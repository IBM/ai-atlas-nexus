NEXUS_URI = "https://w3id.org/ai-atlas-nexus/"


class SPARQLQueryBuilder:
    PREFIXES = f"""
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX nexus: <{NEXUS_URI}>
    PREFIX ex:  <http://example.org/>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    """

    def __init__(self, graph_a: str | None = None, graph_b: str | None = None):
        self.graph_a = graph_a
        self.graph_b = graph_b

    def _header(self) -> str:
        return self.PREFIXES

    def _wrap(self, body: str) -> str:
        return self._header() + body

    def get_all_classes(self):
        """
        Get all classes
        """
        return self._wrap(f"""
            SELECT DISTINCT ?class WHERE {{
            {{
                ?class a rdfs:Class .
            }} UNION {{
                ?class a owl:Class .
            }} UNION {{
                ?instance a ?class .
                FILTER(?class != owl:NamedIndividual)
            }}
            }}
            ORDER BY ?class
        """)

    def get_all_instances_of_class(
        self, class_name_camel, taxonomy, vocabulary, document
    ):
        """
            Get all instances of class

            Args:
                class_name_camel: str | None
                    Name of the class to retrieve
                taxonomy: str | None
                    (Optional) Filter by taxonomy id
                vocabulary: str | None
                    (Optional) Filter by vocabulary id
                document: str | None
                    (Optional) Filter by document id
        ):
        """
        if isinstance(class_name_camel, str):
            class_name_camel = [class_name_camel]

        type_filters = " UNION ".join(
            f"{{ ?s rdf:type nexus:{cls} .}}" for cls in class_name_camel
        )

        query_parts = [f"""SELECT ?s WHERE {{"""]

        if class_name_camel:
            query_parts.append(f" {{ {type_filters} }}")

        if taxonomy:
            query_parts.append(
                f"""?s nexus:isDefinedByTaxonomy "{taxonomy}" . """
            )
        if vocabulary:
            query_parts.append(
                f"""?s nexus:isDefinedByVocabulary "{vocabulary}" . """
            )
        if document:
            query_parts.append(
                f"""?s nexus:hasDocumentation "{document}" . """
            )

        query_parts.append(f"""}}""")

        query = "".join(query_parts)

        return self._wrap(query)

    def get_instances_by_attribute(
        self,
        class_name_camel: str | list[str],
        attribute: str,
        sparql_value: str,
    ) -> str:
        """Get instances of a class that match a specific attribute value.

        Args:
            class_name_camel: Camel case class name (e.g., 'Risk', 'Action')
            attribute: Attribute name to filter by
            sparql_value: Pre-formatted SPARQL value (e.g., '"true"^^xsd:boolean', '"hello"')

        Returns:
            SPARQL query string
        """
        if isinstance(class_name_camel, str):
            class_name_camel = [class_name_camel]

        type_filters = " UNION ".join(
            f"{{ ?s rdf:type nexus:{cls} .}}" for cls in class_name_camel
        )
        return self._wrap(f"""
        SELECT ?s WHERE {{
            {{ {type_filters} }}
            ?s nexus:{attribute} {sparql_value} .
        }}
        """)

    def get_instances_by_attributes(
        self, class_name_camel: str | list[str], filters: dict
    ) -> str:
        """Get instances of a class matching multiple attribute filters (AND).

        Args:
            class_name_camel: Camel case class name (e.g., 'Risk', 'Action')
            filters: Dict of {attribute_name: sparql_literal_value} pairs

        Returns:
            SPARQL query string
        """

        if isinstance(class_name_camel, str):
            class_name_camel = [class_name_camel]

        type_filters = " UNION ".join(
            f"{{ ?s rdf:type nexus:{cls} .}}" for cls in class_name_camel
        )

        query_parts = [f"SELECT ?s WHERE {{"]
        query_parts.append(f" {{ {type_filters} }}")
        for attr, sparql_val in filters.items():
            query_parts.append(f"?s nexus:{attr} {sparql_val} .")
        query_parts.append("}")
        return self._wrap(" ".join(query_parts))

    def intersection(self) -> str:
        return self._wrap(f"""
        SELECT ?s ?p ?o WHERE {{
            GRAPH <{self.graph_a}> {{ ?s ?p ?o }}
            GRAPH <{self.graph_b}> {{ ?s ?p ?o }}
        }}
        """)

    def a_minus_b(self) -> str:
        return self._wrap(f"""
        SELECT ?s ?p ?o WHERE {{
            GRAPH <{self.graph_a}> {{ ?s ?p ?o }}
            FILTER NOT EXISTS {{ GRAPH <{self.graph_b}> {{ ?s ?p ?o }} }}
        }}
        """)

    def b_minus_a(self) -> str:
        return self._wrap(f"""
        SELECT ?s ?p ?o WHERE {{
            GRAPH <{self.graph_b}> {{ ?s ?p ?o }}
            FILTER NOT EXISTS {{ GRAPH <{self.graph_a}> {{ ?s ?p ?o }} }}
        }}
        """)

    def symmetric_difference(self) -> str:
        return self._wrap(f"""
        SELECT ?s ?p ?o ?source WHERE {{
            {{
                GRAPH <{self.graph_a}> {{ ?s ?p ?o }}
                FILTER NOT EXISTS {{ GRAPH <{self.graph_b}> {{ ?s ?p ?o }} }}
                BIND("A only" AS ?source)
            }}
            UNION
            {{
                GRAPH <{self.graph_b}> {{ ?s ?p ?o }}
                FILTER NOT EXISTS {{ GRAPH <{self.graph_a}> {{ ?s ?p ?o }} }}
                BIND("B only" AS ?source)
            }}
        }}
        ORDER BY ?source ?s
        """)

    def jaccard(self, graph_a: str, graph_b: str) -> str:
        return self._wrap(f"""
        SELECT
            (COUNT(DISTINCT ?shared)  AS ?intersection_size)
            (COUNT(DISTINCT ?union_s) AS ?union_size)
            (xsd:float(COUNT(DISTINCT ?shared)) /
             xsd:float(COUNT(DISTINCT ?union_s)) AS ?jaccard)
        WHERE {{
            {{
                GRAPH <{self.graph_a}> {{ ?shared_s ?shared_p ?shared_o }}
                GRAPH <{self.graph_b}> {{ ?shared_s ?shared_p ?shared_o }}
                BIND(CONCAT(STR(?shared_s), STR(?shared_p), STR(?shared_o)) AS ?shared)
                BIND(?shared AS ?union_s)
            }}
            UNION
            {{
                GRAPH <{self.graph_a}> {{ ?a_s ?a_p ?a_o }}
                FILTER NOT EXISTS {{ GRAPH <{self.graph_b}> {{ ?a_s ?a_p ?a_o }} }}
                BIND(CONCAT(STR(?a_s), STR(?a_p), STR(?a_o)) AS ?union_s)
            }}
            UNION
            {{
                GRAPH <{self.graph_b}> {{ ?b_s ?b_p ?b_o }}
                FILTER NOT EXISTS {{ GRAPH <{self.graph_a}> {{ ?b_s ?b_p ?b_o }} }}
                BIND(CONCAT(STR(?b_s), STR(?b_p), STR(?b_o)) AS ?union_s)
            }}
        }}
        """)

    def bfs_frontier(self, frontier_uris):
        """
        BFS

        Args:
            frontier_uris: list[str]
        Return:
            str
        """
        values = " ".join(f"(<{u}>)" for u in frontier_uris)
        return self._wrap(f"""
        SELECT ?s ?p ?o WHERE {{
            VALUES (?s) {{ {values} }}
            ?s ?p ?o .
        }}
        """)

    def get_by_subject(self, subject_uri: str) -> str:
        """All triples where ?s is the given node."""
        return self._wrap(f"""
        SELECT ?p ?o WHERE {{
            <{subject_uri}> ?p ?o .
        }}
        """)

    def get_by_predicate(self, predicate_uri: str) -> str:
        """All triples using the given predicate."""
        return self._wrap(f"""
        SELECT ?s ?o WHERE {{
            ?s <{predicate_uri}> ?o .
        }}
        """)

    def get_by_object(self, object_uri: str) -> str:
        """All triples pointing to the given object."""
        return self._wrap(f"""
        SELECT ?s ?p WHERE {{
            ?s ?p <{object_uri}> .
        }}
        """)

    def get_by_subject_and_predicate(
        self, subject_uri: str, predicate_uri: str
    ) -> str:
        """All objects for a given subject + predicate pair."""
        return self._wrap(f"""
        SELECT ?o WHERE {{
            <{subject_uri}> <{predicate_uri}> ?o .
        }}
        """)

    def get_by_predicate_and_object(
        self, predicate_uri: str, object_uri: str
    ) -> str:
        """All subjects that share the same predicate + object."""
        return self._wrap(f"""
        SELECT ?s WHERE {{
            ?s <{predicate_uri}> <{object_uri}> .
        }}
        """)

    def get_neighbours(self, node_uri: str) -> str:
        """All nodes directly connected to the given node (outgoing edges)."""
        return self._wrap(f"""
        SELECT ?p ?neighbour WHERE {{
            <{node_uri}> ?p ?neighbour .
        }}
        """)

    def get_incoming(self, node_uri: str) -> str:
        """All nodes that point to the given node (incoming edges)."""
        return self._wrap(f"""
        SELECT ?s ?p WHERE {{
            ?s ?p <{node_uri}> .
        }}
        """)

    def get_all_predicates(self) -> str:
        """Distinct predicates used across the entire graph."""
        return self._wrap("""
        SELECT DISTINCT ?p WHERE {
            ?s ?p ?o .
        }
        ORDER BY ?p
        """)

    def get_all_subjects(self) -> str:
        """Distinct subjects across the entire graph."""
        return self._wrap("""
        SELECT DISTINCT ?s WHERE {
            ?s ?p ?o .
        }
        ORDER BY ?s
        """)

    def get_all_objects(self) -> str:
        """Distinct objects across the entire graph."""
        return self._wrap("""
        SELECT DISTINCT ?o WHERE {
            ?s ?p ?o .
        }
        ORDER BY ?o
        """)

    def get_node_degree(self, node_uri: str) -> str:
        """Out-degree and in-degree for a given node."""
        return self._wrap(f"""
        SELECT
            (COUNT(DISTINCT ?out) AS ?out_degree)
            (COUNT(DISTINCT ?in)  AS ?in_degree)
        WHERE {{
            {{
                <{node_uri}> ?p1 ?out .
            }}
            UNION
            {{
                ?in ?p2 <{node_uri}> .
            }}
        }}
        """)

    def get_neighbours_with_hops(self, node_uri: str) -> str:
        """Neighbours"""
        return self._wrap(f"""
            SELECT DISTINCT ?neighbour ?depth
            WHERE {{
                          {{
                    nexus:{node_uri} ?p1 ?neighbour .
                    BIND(1 AS ?depth)
                }}
                UNION
                {{
                    nexus:{node_uri}  ?p1 ?mid1 .
                    ?mid1 ?p2 ?neighbour .
                    BIND(2 AS ?depth)
                }}
                UNION
                {{
                    nexus:{node_uri}  ?p1 ?mid1 .
                    ?mid1 ?p2 ?mid2 .
                    ?mid2 ?p3 ?neighbour .
                    BIND(3 AS ?depth)
                }}

                FILTER(?neighbour != nexus:{node_uri} )
                FILTER(isIRI(?neighbour))
                }}
            ORDER BY ?depth
            """)

    def get_types_for_subjects(self, subject_uris: list) -> str:
        """Get rdf:type for multiple subjects in a single query.

        Args:
            subject_uris: List[str]
                URIs of subjects to get types for

        Returns:
            SPARQL query string returning (?s ?type) pairs
        """
        values = " ".join(f"(<{u}>)" for u in subject_uris)
        return self._wrap(f"""
        SELECT ?s ?type WHERE {{
            VALUES (?s) {{ {values} }}
            ?s <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?type .
        }}
        """)


def get_neighbours_with_hops(self, node_uri: str) -> str:
    """Neightbours"""
    return self._wrap(f"""
            SELECT DISTINCT ?neighbour ?depth
            WHERE {{
                          {{
                    <{node_uri}> ?p1 ?neighbour .
                    BIND(1 AS ?depth)
                }}
                UNION
                {{
                    <{node_uri}> ?p1 ?mid1 .
                    ?mid1 ?p2 ?neighbour .
                    BIND(2 AS ?depth)
                }}
                UNION
                {{
                    <{node_uri}> ?p1 ?mid1 .
                    ?mid1 ?p2 ?mid2 .
                    ?mid2 ?p3 ?neighbour .
                    BIND(3 AS ?depth)
                }}

                FILTER(?neighbour != <{node_uri}>)
                FILTER(isIRI(?neighbour))
                }}
            ORDER BY ?depth
            """)

NEXUS_URI = "https://ibm.github.io/ai-atlas-nexus/ontology/"


class SPARQLQueryBuilder:
    PREFIXES = f"""
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX nexus: <{NEXUS_URI}>
    PREFIX ex:  <http://example.org/>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    """

    def __init__(self, graph_a: str | None = None, graph_b: str | None = None):
        self.graph_a = graph_a
        self.graph_b = graph_b

    def _header(self) -> str:
        return self.PREFIXES

    def _wrap(self, body: str) -> str:
        return self._header() + body

    def get_all_instances_of_class(self, class_name_camel):
        """
        Get all instances of class
        class_name_camel
        """
        return self._header() + f"""
            SELECT ?s WHERE {{
                ?s rdf:type nexus:{class_name_camel} .
            }}
            """

    def get_instances_by_attribute(self, class_name_camel: str, attribute: str, sparql_value: str) -> str:
        """Get instances of a class that match a specific attribute value.

        Args:
            class_name_camel: Camel case class name (e.g., 'Risk', 'Action')
            attribute: Attribute name to filter by
            sparql_value: Pre-formatted SPARQL value (e.g., '"true"^^xsd:boolean', '"hello"')

        Returns:
            SPARQL query string
        """
        return self._wrap(f"""
        SELECT ?s WHERE {{
            ?s rdf:type nexus:{class_name_camel} .
            ?s nexus:{attribute} {sparql_value} .
        }}
        """)


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

    def get_by_subject_and_predicate(self, subject_uri: str, predicate_uri: str) -> str:
        """All objects for a given subject + predicate pair."""
        return self._wrap(f"""
        SELECT ?o WHERE {{
            <{subject_uri}> <{predicate_uri}> ?o .
        }}
        """)

    def get_by_predicate_and_object(self, predicate_uri: str, object_uri: str) -> str:
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

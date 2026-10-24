"""Helpers for the SSSOM mapping files in ``data/mappings``."""

from sssom.constants import (
    NO_TERM_FOUND,
    OBJECT_ID,
    PREDICATE_MODIFIER,
    PREDICATE_MODIFIER_NOT,
    SUBJECT_ID,
)
from sssom.util import MappingSetDataFrame


def drop_no_match_rows(msdf: MappingSetDataFrame) -> MappingSetDataFrame:
    """Return the mapping set without the rows that record no match.

    A row records no match when its predicate_modifier is Not, or when its
    subject or object is sssom:NoTermFound. The lift script and
    load_curated_mappings both call this function, so the graph and the
    evaluation's ground truth leave out the same rows.

    Args:
        msdf: MappingSetDataFrame
            A mapping set parsed from an SSSOM/TSV file.

    Returns:
        MappingSetDataFrame: a new mapping set that holds the other rows.
    """
    df = msdf.df
    keep = (df[SUBJECT_ID] != NO_TERM_FOUND) & (df[OBJECT_ID] != NO_TERM_FOUND)
    if PREDICATE_MODIFIER in df.columns:
        keep &= df[PREDICATE_MODIFIER] != PREDICATE_MODIFIER_NOT
    return MappingSetDataFrame(
        df=df[keep], converter=msdf.converter, metadata=msdf.metadata
    )

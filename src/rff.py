from collections import defaultdict


def rff(rankings, k=60):
    """
    Calculate the Reciprocal Rank Fusion (RRF) score for a list of rankings.

    Parameters:
    - rankings: List of lists, where each inner list contains ranked items.
    - k: A constant used in the RRF formula (default is 60).

    Returns:
    - List of tuples containing item and its RRF score, sorted by score in descending order.
    """

    rrf_scores = defaultdict(float)

    for rank_list in rankings:
        for i, item in enumerate(rank_list):
            rrf_scores[item] += 1 / (k + i + 1)

    return sorted(rrf_scores.items(), key=lambda x: x[1], reverse=True)

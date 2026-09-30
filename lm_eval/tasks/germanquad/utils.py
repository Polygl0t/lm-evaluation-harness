import transformers.data.metrics.squad_metrics as squad_metrics


def process_results_germanquad(doc, results):
    # squad_metrics normalisation (lowercase, strip, collapse whitespace, drop
    # punctuation), as in xquad/mlqa's process_results_qa. The generic exact_match
    # metric never strips whitespace, so it scored 0 for every completion.
    # The test split has up to three references; score against the best match.
    pred = results[0]
    references = doc["answers"]["text"]
    return {
        "exact_match": max(squad_metrics.compute_exact(ref, pred) for ref in references),
        "f1": max(squad_metrics.compute_f1(ref, pred) for ref in references),
    }

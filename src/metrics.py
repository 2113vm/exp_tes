import Levenshtein


def text_recognition_score(target_text: str,
                           predicted_text: str) -> dict:

    metrics = [Levenshtein.ratio, Levenshtein.jaro_winkler]

    scores = []

    for metric in metrics:
        scores.append(map(lambda pair: metric(*pair),
                          zip(predicted_text,
                              target_text)))

    return scores

import Levenshtein


def text_recognition_score(target_text: str,
                           predicted_text: str) -> tuple:

    return Levenshtein.ratio(target_text, predicted_text), \
           Levenshtein.jaro_winkler(target_text, predicted_text)

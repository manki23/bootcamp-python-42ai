class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if (
            coefs is None or
            words is None or
            len(coefs) != len(words) or
            len(coefs) < 1 or
            not all(isinstance(coef, float) for coef in coefs) or
            not all(isinstance(word, str) for word in words)
        ):
            print(-1)
        else:
            print(sum(coef * len(word) for coef, word in zip(coefs, words)))

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if (
            coefs is None or
            words is None or
            len(coefs) != len(words) or
            len(coefs) < 1 or
            not all(isinstance(coef, float) for coef in coefs) or
            not all(isinstance(word, str) for word in words)
        ):
            print(-1)
        else:
            enum_list = enumerate(zip(coefs, words))
            print(sum(coef * len(word) for i, (coef, word) in enum_list))

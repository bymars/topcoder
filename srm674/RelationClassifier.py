class RelationClassifier:
    def isBijection(self, domain, _range):
        l = len(domain)
        for i in range(l):
            for j in range(l):
                if domain[i] == domain[j] and _range[i] != _range[j]:
                    return "Not"
                if _range[i] == _range[j] and domain[i] != domain[j]:
                    return "Not"
        return "Bijection"

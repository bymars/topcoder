class SimilarUserDetection:
    def haveSimilar(self, handles):
        for i in range(0, len(handles)):
            handles[i] = handles[i].replace('O', '0').replace('I', '1').replace('l', '1')
        for i in range(0, len(handles)):
            for j in range(i+1, len(handles)):
                if handles[i] == handles[j]:
                    return "Similar handles found"
        return "Similar handles not found"

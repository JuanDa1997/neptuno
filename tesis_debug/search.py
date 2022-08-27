from googlesearch import search
# search the voice command in google


class searching_google:
    match = ''
    counter = 0
    arrMatch = []
    borrar = ''

    def search(self, match):
        for i in search(match):
            self.counter += 1
            if self.counter == 5:
                break
            else:
                # send list of matches to js
                self.arrMatch.append(i)
                # print(i)
        # self.theMatch["match"] = self.arrMatch

        return self.filter(self.arrMatch, self.borrar)

    def filter(self, arrMatch, borrar):

        for i in arrMatch:

            if arrMatch.count(i) >= 2:
                borrar = i
                arrMatch.remove(borrar)

        return arrMatch


""" obj = searching_google()

obj.search('patos') """

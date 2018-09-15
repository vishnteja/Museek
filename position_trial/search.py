
import pprint
import json


def pos_intersect(p1, p2, k):
    answer = []

    doc1 = p1["doc"]
    len1 = len(doc1)
    doc2 = p2["doc"]
    len2 = len(doc2)

    i = j = 0

    while i != len1 and j != len2:

        if doc1[i] == doc2[j]:
            li = []

            pos1 = p1[doc1[i]]
            lp1 = len(pos1)
            pos2 = p2[doc2[j]]
            lp2 = len(pos2)

            ii = jj = 0

            while ii != lp1:

                while jj != lp2:

                    if abs(pos1[ii] - pos2[jj]) <= k:

                        li.append(pos2[jj])

                    elif pos2[jj] > pos1[ii]:
                        break

                    jj += 1

                while li != [] and abs(li[0] - pos1[ii]) > k:
                    li.remove(li[0])

                for ps in li:
                    answer.append([doc1[i], pos1[ii], ps])

                ii += 1
            i += 1

            j += 1

        elif doc1[i] < doc2[j]:
            i += 1

        else:
            j += 1

    return answer


print("Loading Index...")
with open("index.json") as f:
    ans = json.load(f)

print("Load Complete")


i = 1


while i == 1:
    phrase1 = input("Enter First Search Query: ")

    phrase2 = input("Enter Second Search Query: ")

    k = int(input("Input k value: "))

    pprint.pprint(pos_intersect(ans[phrase1], ans[phrase2], k))

    check = input("\n Another Query? (Y/n)")

    if check == 'n':
        break

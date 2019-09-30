class Node:
    def __init__(self):
        self.next = dict()
        self.same = 1

def make_tree(words,root):
    for word in words:
            search = root
            for w in word:
                if w in search.next:
                    search = search.next[w]
                    search.same += 1
                else:
                    search.next[w] = Node()
                    search = search.next[w]         
    return root
def make_reverse_tree(words,root):
    for word in words:
        search = root
        for w in reversed(word):
            if w in search.next:
                search = search.next[w]
                search.same += 1
            else:
                search.next[w] = Node()
                search = search.next[w]
    return root

def get_child(node, n):
    if n == 0 and not node.next:
        return node.same
        
    count = 0
    for d in node.next.values():
        count += get_child(d, n-1)
    return count
        

def solution(words,queries):
    answer = []
    front, end = Node(), Node()
    front = make_tree(words,front)
    end = make_reverse_tree(words,end)
    
    for query in queries:
        if query[0] != '?': # front
            search = front
            for q in query:
                if q != '?': 
                    if q in search.next:
                        search = search.next[q]
                    else : answer.append(0); break
                else:
                    answer.append(get_child(search,query.count('?')))
                    break
        else: # back
            search = end
            for q in reversed(query):
                if q != '?': 
                    if q in search.next:
                        search = search.next[q]
                    else : answer.append(0); break
                else:
                    answer.append(get_child(search,query.count('?')))
                    break
    return answer
    
if __name__ == "__main__":
    words = ['frodo','front','frost','frozen','frame','kakao']
    queries = ['fro??','????o','fr???','fro???','pro?']
    print(solution(words,queries))

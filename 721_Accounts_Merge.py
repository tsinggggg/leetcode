class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        out = []
        email_to_email = collections.defaultdict(set)
        email_to_name = {}
        
        for ind, a in enumerate(accounts):
            emails = a[1: ]
            email0 = a[1]
            for email in emails:
                email_to_email[email].add(email0)
                email_to_email[email0].add(email)
                email_to_name[email] = a[0]

        
        visited = []
        for i in email_to_email.keys():
            
            if i not in visited:
                
                queue = [i]
                bfs_visited = [i]
                
                while queue:
                    
                    curr = queue[0]
                    queue = queue[1:]
                    nb = email_to_email[curr]
                    for n in nb:
                        if n not in bfs_visited:
                            bfs_visited.extend(nb)
                            queue.extend(nb)
   
                visited.extend(bfs_visited)
                out.append(merge(bfs_visited, email_to_name))

        return out 

                
                        
                        
def merge(bfs_visited, email_to_name):
    name = email_to_name[bfs_visited[0]]
    emails = sorted(list(set(bfs_visited)))
    return [name] + emails



# no need to look back when going through all accounts
# the connection info is within per account
# boil downs to a finding connected components in graph problem
        
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        def buildGraph(equations, values, gr):
            for i, eq in enumerate(equations):
                divident = eq[0]
                divisor = eq[1]
                if divident not in gr:
                    gr[divident] = {}
                if divisor not in gr:
                    gr[divisor] = {}
                
                gr[divident][divisor] = values[i]
                gr[divisor][divident] = 1 / values[i]

            return gr
        
        gr = buildGraph(equations, values, {})

        def dfs(node, divisor, gr, vis, ans, t):
            if node in vis:
                return
            
            if node == divisor:
                ans[0] = t
                return
            
            vis.add(node)
            # Traverse
            for nextNode, val in gr[node].items():
                dfs(nextNode, divisor, gr, vis, ans, val * t)
        
        answers = []
        for query in queries:
            vis = set()
            ans = [-1.0]
            divident = query[0]
            divisor = query[1]
            if divident not in gr:
                answers.append(ans[0])
                continue 
            if divisor not in gr:
                answers.append(ans[0])
                continue 
            t = 1.0
            dfs(divident, divisor, gr, vis, ans, t)
            answers.append(ans[0])

        return answers










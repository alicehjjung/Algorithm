class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.dfs(image, sr,sc,image[sr][sc],color)
        return image

    def dfs(self, image, sr, sc, curr_color, color):
        if 0<=sr<len(image) and 0<=sc<len(image[0]) and image[sr][sc] == curr_color and image[sr][sc]!=color:
            image[sr][sc] = color

            self.dfs(image,sr-1,sc,curr_color,color)
            self.dfs(image,sr,sc-1,curr_color,color)
            self.dfs(image,sr+1,sc,curr_color,color)
            self.dfs(image,sr,sc+1,curr_color,color)

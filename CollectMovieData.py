import httplib2, json

class CollectMovieData:
    def __init__(self):
        self.movie_title_set = set()
        self.base_url = "http://www.omdbapi.com/?t=%s&y&plot=short&r=json"
        self.h = httplib2.Http(".cache")

    def main(self):
        self.collect_movies_set()
        self.get_movie_more_info()

    def collect_movies_set(self):
        with open('movies.list.2015','r') as f:
            for line in f.readlines():
                try:
                    movie_title = line.split('(')[0].strip().strip('"').strip('#')
                    self.movie_title_set.add(movie_title.lower().replace(' ','+'))
                except:
                    continue

    def get_movie_more_info(self):
        with open('movies.info.2015','w') as f:
            for movie_title in self.movie_title_set:
                try:
                    fire_url = self.base_url % (movie_title)
                    resp, content = self.h.request(fire_url)
                    if not 'Error' in content:
                        print content
                    json.dump(f,content)
                except:
                    continue 
            


if __name__ == "__main__":
    cmd = CollectMovieData()
    cmd.main()

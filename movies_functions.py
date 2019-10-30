 def get_score(movie):
        metascores = []

        for score in movie:
            metascore1 = score.find(class_="metascore")
            if metascore1 == 'None':
                metascore = 'None'
            else:
                try: 
                    metascores.append(int(metascore1.get_text()[:2]))
#                     metascore = metascore1.get_text()
                except:
                    metascores.append(0)
            
        return metascores
    
# print(get_score(movie))

var = 51
while var < 500: 
    page = requests.get(f"https://www.imdb.com/search/title/?title_type=feature&year=2018-01-01,2018-12-31&sort=boxoffice_gross_us,desc&start={var}&ref_=adv_nxt")
    soup = BS(page.content, 'html.parser')
    soup.prettify()
    info = soup.find_all(id = 'main')
    movie = info[0].find_all(class_='lister-item mode-advanced')
    movie_df = make_df(movie)
    insert_movies(movie_df)
#     print(movie_df)
    var +=50

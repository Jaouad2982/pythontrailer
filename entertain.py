import media
# import media file
import fresh_tomatoes
# import fresh_tomatoes.py which is a python file with html
# and css + javascript and also python
# name of the movies and also their details title, link of pic, link of video
mrnobody = "Nemo shares his story with a reporter and reviews "
theseventhseal = " was such a perfect film, this one would have to be a winner"

mrNobody = media.Movie(" Mr nobody", mrnobody,
                       "http://www.undertheradarmag.com/uploads/review_images/"
                       "mr-nobody.jpg",
                       "https://www.youtube.com/watch?v=mpi0qsp3v_w")

edward_Scissorhands = media.Movie("Edward Scissorhands",
                                  "An inner conflict between love",
                                  "http://digitalspyuk.cdnds.net/15/50/"
                                  "980x490/landscape-1449768828-"
                                  "johnny-depp-edward-scissorhands.jpg",
                                  "https://www.youtube.com/"
                                  "watch?v=M94yyfWy-KI")
theSeventh_seal = media.Movie("The seven seal", theseventhseal,
                              "https://www.santamonica.com/wp-content/uploads/"
                              "2017/01/The_Seventh_Seal.jpg",
                              "https://www.youtube.com/watch?v=1qjUIwGaMAs")
ugetsu_Monogatari = media.Movie("Ugetsu Ugetsu Monogatari", "A conflict"
                                "between greed and envy",
                                "https://cdn-3.cinemaparadiso.co.uk/clp/"
                                "546049-20652-clp-950.jpg",
                                "https://www.youtube.com/watch?v=cgBHeJfnJ5s")
the_departed = media.Movie("The departed", "two different minds",
                           "http://cdn3.thr.com/sites/default/"
                           "files/imagecache/"
                           "landscape_928x523/2016/10/"
                           "the_departed_-_h_-_2006.jpg",
                           "https://www.youtube.com/watch?v=iQpb1LoeVUc")
the_others = media.Movie("The others", "return from war.",
                         "http://1125996089.rsc.cdn77.org/wp-content/uploads/"
                         "2017/07/Others_2001_56.jpg",
                         "https://www.youtube.com/watch?v=0bMEGtUxajY")
the_usual_suspects = media.Movie("the usual suspects", "a fire aboard a ship",
                                 "http://images.mentalfloss.com/sites/default/"
                                 "files/usual_lg_0.jpg?resize=1100x740",
                                 "https://www.youtube.com/watch?v=9MjV4EwR7Mg")
the_chaser = media.Movie("the chaser", "A detective story",
                         "http://img.affenheimtheater.de/cover_br/image.php/"
                         "cover_the_chaser_fr."
                         "jpg?height=460&width=540&image=/cover_br/"
                         "cover_the_chaser_fr.jpg",
                         "https://www.youtube.com/watch?v=7EVIWX6EGCk")
movies = [mrNobody, edward_Scissorhands, theSeventh_seal, ugetsu_Monogatari,
          the_departed, the_others, the_usual_suspects, the_chaser]
# a list called movies that has all the movies listed above
fresh_tomatoes.open_movies_page(movies)
# a method called open which imported from fresh tomatoes
# with the role of opening the list and displat the movies

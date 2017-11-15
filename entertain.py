import media
import fresh_tomatoes
import webbrowser
mrNobody = media.Movie(" Mr nobody","On his deathbed, Nemo shares his story with a reporter and reviews the choices he made along the way.",
                           "http://www.undertheradarmag.com/uploads/review_images/mr-nobody.jpg","https://www.youtube.com/watch?v=mpi0qsp3v_w")
edward_Scissorhands = media.Movie("Edward Scissorhands","An inner conflict between love,desir and difference .At first, everyone welcomes him into his new community, but soon things begin to take a change for the worst",
                                      "http://digitalspyuk.cdnds.net/15/50/980x490/landscape-1449768828-johnny-depp-edward-scissorhands.jpg","https://www.youtube.com/watch?v=M94yyfWy-KI")
theSeventh_seal = media.Movie("The seven seal","If there ever was such a thing as a perfect film, this one would have to be a winner. never seen such a perfection in picture that was so moving, well shot, written, acted",
                                  "https://www.santamonica.com/wp-content/uploads/2017/01/The_Seventh_Seal.jpg","https://www.youtube.com/watch?v=1qjUIwGaMAs")
ugetsu_Monogatari = media.Movie("Ugetsu (Ugetsu Monogatari)","A conflict between greed and envy, an inner fight between love, and love of familty in the midst of a very devastating war",
                                    "https://cdn-3.cinemaparadiso.co.uk/clp/546049-20652-clp-950.jpg","https://www.youtube.com/watch?v=cgBHeJfnJ5s")
the_departed = media.Movie("The departed","The film revolves around two people who have two totally different backgrounds but a thing in common is their job  spy. Billy Costigan, an undercovered cop and a police officer",
                               "http://cdn3.thr.com/sites/default/files/imagecache/landscape_928x523/2016/10/the_departed_-_h_-_2006.jpg","https://www.youtube.com/watch?v=iQpb1LoeVUc")
the_others = media.Movie("The others","Nicole Kidman a mother of two, who is awaiting her husband's return from war. When a new trio of servants arrives to replace the crew that inexplicably disappeared,",
                         "http://1125996089.rsc.cdn77.org/wp-content/uploads/2017/07/Others_2001_56.jpg","https://www.youtube.com/watch?v=0bMEGtUxajY")
the_usual_suspects = media.Movie("the usual suspects","A firefight and a fire aboard a ship docked in the San Pedro Bay leaves only two survivors: a Hungarian criminal named Arkos Kovaz who hospitalizes because of severe burns and others",
                                 "http://images.mentalfloss.com/sites/default/files/usual_lg_0.jpg?resize=1100x740","https://www.youtube.com/watch?v=9MjV4EwR7Mg")
the_chaser = media.Movie("the chaser","A dirty detective turned pimp in financial trouble as several of his girls have recently disappeared without clearing their debts","http://img.affenheimtheater.de/cover_br/image.php/cover_the_chaser_fr.jpg?height=460&width=540&image=/cover_br/cover_the_chaser_fr.jpg","https://www.youtube.com/watch?v=7EVIWX6EGCk")
movies = [mrNobody , edward_Scissorhands ,theSeventh_seal ,ugetsu_Monogatari ,the_departed ,the_others ,the_usual_suspects ,the_chaser]
fresh_tomatoes.open_movies_page(movies)

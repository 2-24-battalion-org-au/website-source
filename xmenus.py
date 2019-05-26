

import human2website.builder.menu as menu



HOMEBUTTON={ 'url':'/index.html',
             'button':[ [ menu.Img, '/images/menu_d_patch.png' ],
                        [ menu.Html, '2/24th Battalion' ],
                        [ menu.Img, '/images/menu_t_patch.png' ],
                      ]
           }



menutop={ 'home':HOMEBUTTON,
          'sticky':True,
          'menu':[ [ menu.Submenu, 'About',
                     [ [ menu.Link, '/association.html','The Association'],
                       [ menu.Link, '/memwall.html','Memorial wall'],
                       [ menu.Link, '/committee.html','Committee'],
                       [ menu.Link, '/contacts.html','Contacts'],
                       [ menu.Link, '/products.html','Products'],
                       [ menu.Link, '/fflyer.html','Furphy Flyer'],
                       [ menu.Rule ],
                       [ menu.Link, '/links.html','External Links'],
                     ],
                   ],
                   [ menu.Submenu, 'History',
                     [ [ menu.Link, '/history.html','History of the 2/24th'],
                       [ menu.Link, '/patches.html','Colour patches'],
                       [ menu.Rule, ],
                       [ menu.Link, '/lecture.html','Lectures and talks'],
                       [ menu.Link, '/stories.html','Stories'],
                       [ menu.Link, '/memories.html','Memories'],
                       [ menu.Rule, ],
                       [ menu.Link, '/bibliography.html','Bibliography'],
                       [ menu.Link, '/reviews.html','Reviews'],
                     ],
                   ],
                   [ menu.Submenu, 'Rolls',
                     [ [ menu.Link, '/rolls/index.html','Rolls'],
                       [ menu.Link, '/vale.html','Vale'],
                       [ menu.Rule, ],
                       [ menu.Link, '/archives.html','Searching Archives'],
                     ],
                   ],
                   [ menu.Link, '/gallery.html','Gallery'],
                 ],
        }




menubottom={ 'home':HOMEBUTTON,
             'valign':'bottom',
             'menu':[
               [ menu.Link,'/sitemap.html','Sitemap' ],
               [ menu.Link,'/credits.html','Credits' ],
               [ menu.Html,'ABN 44 692 430 316' ],
             ],
             'menuright':[
               [ menu.Html,'Design by Arramlu<br /> &copy; 2008-2019 2/24th Battalion Association Inc' ],
               [ menu.Link,'mailto:webmaster@2-24.battalion.org.au','contact<br/>webmaster@2-24.battalion.org.au' ],
             ],
           }




import os
import sys
sys.path.append('..')

import human2website.builder as builder
import human2website.toolkits
import human2website.toolkits.bootstrap4
import human2website.toolkits.bootstrap4.dualmenu

import xmenus


toolkit=human2website.toolkits.bootstrap4.dualmenu.DualMenu()



ht=builder.HumanTree(toolkit,'webpages/','../2-24.battalion.org.au/www')



toolkit.setting('menutop', toolkit.menu2html( xmenus.menutop ) )
toolkit.setting('menubottom', toolkit.menu2html( xmenus.menubottom ) )
toolkit.setting('title','2-24th Battalion Association')
toolkit.setting('keywords',"Tobruk, 2nd AIF, Tel El Eisa, El Alamein, Rats of Tobruk, World War 2, ANZAC, Australian Army, 9th Division, Salient, Halfaya Pass, Tarakan, New Guinea, Finschhafen, Lae, Wangaratta's Own")



ht.precopy('/.build.txt')
ht.website_info('/whoami.txt',"i am generated via cam's magic and stored on appengine")

ht.precopy('/CNAME')
ht.precopy('/Notice of Meeting.docx')
ht.build_final()



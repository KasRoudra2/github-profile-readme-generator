import os, sys
os.system("clear")
os.system("figlet SetProfile")
print("Enter a one line bio!")
bio=input()
os.system("sleep 2")
print("\nEnter a profile view according to your wish.\nGive a trustworthy number!")
prnm=input()
os.system("sleep 2")
print("\nEnter number of codes you've written.\nGive a trustworthy number!")
cd=input()
os.system("sleep 2")
print("\nWrite four paragraphs about you. Press enter only if a paragraph completes!")
os.system("sleep 2")
print('''\n\nExample for you-
1. Learning programming languages: HTML, CSS, JavaScript, C, Python, Bash/Shell
2. Hobby: Reading books, Listen music, Play games.
3. Loves to: Create Ebooks, Ringtones, Fake Screenshots, Memes, Meme Templates.
4. Experienced in: Phone Rooting, Custom Rom/Recovery, Install OS in PC.\n
Now write:''')
p1=input()
p2=input()
p3=input()
p4=input()
os.system("sleep 2")
print("\nEnter up to 6 programming/web developing languages:")
os.system("sleep 2")
print("\nAvailable languages:\n1.html5\n2.css3\n3.javascript\n4.python\n5.shell\n6.c\n7.java\n8.php\n9.swift\n10.csharp\n11.ruby\n12.cpluplus\n13.dart\n14.go\n18.haskell\n19.bootstrap\n20.mysql\n21.r\n22.jquery\n\nWrite:")
ic1=input()
ic2=input()
ic3=input()
ic4=input()
ic5=input()
ic6=input()
os.system("sleep 2")
print("\nEnter your github username:")
git=input()
os.system("sleep 2")
print("\nWrite theme names correctly for four images.")
os.system("sleep 2")
print("\n1.dark\n2.highcontrast\n3.radical\n4.merko\n5.gruvbox\n6.gruvbox_duo\n7.tokyonight\n8.tokyonight_duo\n9.onedark\n10.onedark_duo\n11.solarized-dark\n12.vue\n13.vue-dark\n14.monokai\n15.buefy\n16.cobalt\n17.synthwave\n18.dracula\n19.prussian\n20.graywhite\n21.blueberry\n22.kacho-ga\n23.black-ice\n24.yeblu\n25.slateorange\n26.ads-juicy-fresh\n27.maroongold\n28.joly\n29.algolia\n30.graywhite")
os.system("sleep 2")
print("\nTop Languages:")
lang=input()
print("\n1.dark\n2.highcontrast\n3.radical\n4.merko\n5.gruvbox\n6.gruvbox_duo\n7.tokyonight\n8.tokyonight_duo\n9.onedark\n10.onedark_duo\n11.solarized-dark\n12.vue\n13.vue-dark\n14.monokai\n15.buefy\n16.cobalt\n17.synthwave\n18.dracula\n19.prussian\n20.graywhite\n21.blueberry\n22.kacho-ga\n23.black-ice\n24.yeblu\n25.slateorange\n26.ads-juicy-fresh\n27.maroongold\n28.joly\n29.algolia\n30.graywhite")
os.system("sleep 2")
print("\nSteak and Contributions:")
stk=input()
print("\n1.dark\n2.highcontrast\n3.radical\n4.merko\n5.gruvbox\n6.gruvbox_duo\n7.tokyonight\n8.tokyonight_duo\n9.onedark\n10.onedark_duo\n11.solarized-dark\n12.vue\n13.vue-dark\n14.monokai\n15.buefy\n16.cobalt\n17.synthwave\n18.dracula\n19.prussian\n20.graywhite\n21.blueberry\n22.kacho-ga\n23.black-ice\n24.yeblu\n25.slateorange\n26.ads-juicy-fresh\n27.maroongold\n28.joly\n29.algolia\n30.graywhite")
os.system("sleep 2")
print("\nCommits:")
com=input()
print("\n1.dark\n2.highcontrast\n3.radical\n4.merko\n5.gruvbox\n6.gruvbox_duo\n7.tokyonight\n8.tokyonight_duo\n9.onedark\n10.onedark_duo\n11.solarized-dark\n12.vue\n13.vue-dark\n14.monokai\n15.buefy\n16.cobalt\n17.synthwave\n18.dracula\n19.prussian\n20.graywhite\n21.blueberry\n22.kacho-ga\n23.black-ice\n24.yeblu\n25.slateorange\n26.ads-juicy-fresh\n27.maroongold\n28.joly\n29.algolia\n30.graywhite")
os.system("sleep 2")
print("\nTrophy:")
trp=input()
os.system("rm -rf README.md")
prof= open("README.md",'a')
print('''<h1 align="center">Hi visitor, I am '''+git+'''.
Welcome to my profile!</h1>
<h2 align="center">'''+bio+'''</h2>
<p align="center">
<img src="https://img.shields.io/badge/Profile%20Views-'''+prnm+'''-blue">
<img src="https://img.shields.io/badge/Number%20Of%20Codes%20I've%20written-'''+cd+'''-blue"> 
</p>
<h2 align="center"><u>Personal Details</u></h2>
<p align="center">
'''+p1+'''\n'''+p2+'''\n'''+p3+'''\n'''+p4+'''
</p>
<h3>Languages</h3>
<p align="center">
<img src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/'''+ic1+'''.svg" height="70" width="70">
<img src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/'''+ic2+'''.svg" height="70" width="70">
<img src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/'''+ic3+'''.svg" height="70" width="70">
<img src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/'''+ic4+'''.svg" height="70" width="70">
<img src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/'''+ic5+'''.svg" height="70" width="70">
<img src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/'''+ic6+'''.svg" height="70" width="70">
</p>
<h2 align="center"><u>My Github Stats</u></h2>
<p align="center">
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username='''+git+'''&layout=compact%22&theme='''+lang+'''">
<img src="https://github-readme-streak-stats.herokuapp.com/?user='''+git+'''&theme='''+stk+'''">
<img src="https://github-readme-stats.vercel.app/api?username='''+git+'''&count_private=true&show_icons=true&theme='''+com+'''">
<img src="https://github-profile-trophy.vercel.app/?username='''+git+'''&theme='''+trp+'''">
</p>''', file= prof)
prof.close()
print("README.md file genearated successfully!Check your current directory!")
exit()
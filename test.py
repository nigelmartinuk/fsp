# hardcoded dictionary testing

favs = {
    # key :          { image,                    html }
    "akira":         ["large_akira.jpg",         "akira.html" ],
    "atlantis":      ["large_atlantis.jpg",      "atlantis.html"],
    "cryingfreeman": ["large_cryingfreeman.jpg", "cryingfreeman.html"],
    "fringe":        ["large_fringe.jpg",        "fringe.html"],
    "princessbride": ["large_princessbride.jpg", "princessbride.html"],
    "reddwarf":      ["large_reddwarf.jpg",      "reddwarf.html"],
    "rogueone":      ["large_rogueone.jpg",      "rogueone.html"],
    "sg1":           ["large_sg1.jpg",           "sg1e.html"]
}

# sequentially read favourites dictionary into separate values
for an_entry in favs:
    img, html = favs[an_entry]
    print(f"Image: {img}\nhtml: {html}")

for id, vals in favs.items() :
      v, i = vals
      print(f"v:{v}\ni:{i}")
      
    #   <p>id: {{id}} vals: {{vals}}  Image: {{img}}<br>html: {{html}}</p>
    # </div>
    # {% endfor %}
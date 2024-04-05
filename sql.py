import sqlite3

def init_db(c):
   c.execute(""" DROP TABLE IF EXISTS Restaurant""")
    
   c.execute(""" CREATE TABLE Restaurant(
                  Id INT PRIMARY KEY,
                  Name VARCHAR,
                  City VARCHAR,
                  Address VARCHAR,
                  Cuisine VARCHAR,
                  Phone VARCHAR,
                  Vegetarian INT,
                  Halal INT,
                  Kosher INT,
                  Gluten_Free INT)
              """)

   c.execute(""" INSERT INTO Restaurant VALUES
                     (1, "Canoe Restaurant and Bar", "Toronto", "66 Wellington St. W, Toronto ", "Canadian", "(416) 364-0054", 0, 0, 0, 0), 
                     (2, "Richmond Station", "Toronto", "1 Richmond St. W, Toronto", "American", "(647) 748-1444", 0, 0, 1, 0), 
                     (3, "Oji Seichi", "Toronto", "354 Broadview Ave, Toronto", "Ramen", "(416) 519-4356", 0, 0, 0, 0), 
                     (4, "Grey Gardens", "Toronto", "199 Augusta Ave., Toronto", "Seafood", "(647) 351-1552", 1, 0, 0, 0), 
                     (5, "Sotto Sotto", "Toronto", "120 Avenue Rd., Toronto", "Italian", "(416) 962-0011", 0, 0, 0, 0), 
                     (6, "Alo Restaurant", "Toronto", "163 Spadina Ave., Toronto", "French", "(416) 260-2222", 1, 0, 1, 1), 
                     (7, "Chubby's Jamaican Kitchen", "Toronto", "104 Portland St., Toronto", "Jamaican", "(416) 792-8105", 1, 0, 0, 1), 
                     (8, "Gusto 101", "Toronto", "101 Portland St., Toronto", "Italian", "(416) 504-9669", 1, 0, 1, 1), 
                     (9, "Dreyfus", "Toronto", "96 Harbord St., Toronto", "French", "(416) 323-1385", 1, 1, 0, 0), 
                     (10, "Bar Raval", "Toronto", "505 College St., Toronto", "Mediterranean", "(647) 344-8001", 0, 0, 1, 0), 
                     
                     (11, "IL FORNELLO", "Brock", "300c Fourth Ave, St. Catharines", "Italian", "(905) 684-5000", 1, 1, 0, 1), 
                     (12, "Fat Rabbit", "Brock", "34 Geneva St, St. Catharines", "Burgers", "(905) 688-6553", 1, 0, 0, 1), 
                     (13, "Twenty Kitchen & Bar", "Brock", "259 St Paul St, St. Catharines", "Canadian", "(905) 329-9024", 0, 0, 0, 0), 
                     (14, "HAMBRGR", "Brock", "233 ST PAUL ST, St. Catharines", "Steakhouse", "(289) 362-4440", 0, 0, 0, 0), 
                     (15, "Benchmark", "Brock", "135 Taylor Rd, Niagara-on-the-Lake", "American", "(905) 641-2252", 1, 0, 0, 1), 
                     (16, "MR MIKES", "Brock", "295 4th Avenue, St. Catharines", "Burgers", "(905) 682-1023", 1, 0, 0, 1), 
                     (17, "Solaia Cucina e Cantina", "Brock", "30 St. Paul St., St. Catharines", "Italian", "(905) 378-0040", 1, 0, 1, 1), 
                     (18, "Rockway Vineyards", "Brock", "3290 Ninth Street, St. Catharines", "American", "(905) 641-5771", 0, 0, 1, 0), 
                     (19, "Lake House Restaurant", "Brock", "3100 North Service Road, Vineland", "Mediterranean", "(905) 562-6777", 1, 0, 1, 1), 
                     (20, "Table Rock House Restaurant", "Brock", "6650 Niagara Parkway, Niagara Falls", "Canadian", "(905) 354-3631", 1, 0, 0, 1), 
                     
                     (21, "The Keg Steakhouse + Bar", "Oshawa", "255 Stevenson Rd S, Oshawa", "Steakhouse", "(905) 571-3212", 1, 0, 0, 1), 
                     (22, "Wildfire Oshawa", "Oshawa", "540 King Street West, Oshawa", "Canadian", "(905) 215-0231", 1, 1, 1, 1), 
                     (23, "Baxters Landing", "Oshawa", "419 King St. W, Oshawa", "Canadian", "(905) 215-0132", 1, 0, 0, 1), 
                     (24, "Brock Street Brewing Company", "Oshawa", "244 Brock St S, Whitby", "American", "(833) 276-2578", 1, 0, 0, 1), 
                     (25, "Scaddabush", "Oshawa", "75 Consumers Dr, Whitby", "Italian", "(289) 989-2880", 1, 0, 0, 1), 
                     (26, "Legend of Fazio's", "Oshawa", "33 Simcoe St S, Oshawa", "Italian", "(905) 240-1199", 1, 1, 1, 1), 
                     (27, "Bella Notte Ristorante", "Oshawa", "3570 Brock St N, Whitby", "Italian", "(905) 430-5744", 0, 0, 0, 1), 
                     (28, "Bistro 67", "Oshawa", "1604 Champlain Ave, Whitby", "Canadian", "(905) 721-3312", 0, 0, 1, 0), 
                     (29, "Bâton Rouge Grillhouse & Bar", "Oshawa", "25 Consumers Dr, Whitby", "Steakhouse", "(905) 444-9525", 1, 0, 0, 0), 
                     (30, "Milestones Bar + Grill", "Oshawa", "75 Consumers Dr, Bldg T, Whitby", "Global", "(905) 666-9070", 1, 0, 1, 1), 
                     
                     (31, "Tiny Thai Restaurant", "Burlington", "293 Main Street, Winooski", "Thai", "(802) 655-4888", 1, 0, 1, 1), 
                     (32, "Onion City Chicken & Oyster", "Burlington", "3 E Allen St, Winooski", "French", "(802) 540-8489", 0, 0, 1, 1), 
                     (33, "Misery Loves Co.", "Burlington", "46 Main St (at W Center St), Winooski", "Canadian", "(802) 497-3989", 1, 1, 1, 1), 
                     (34, "Kismayo Kitchen", "Burlington", "505 Riverside Ave (Intervale Rd), Burlington", "Somalian", "(802) 448-3032", 1, 1, 1, 1), 
                     (35, "Taco Gordo", "Burlington", "208 N Winooski Ave, Burlington", "Mexican", "(802) 540-0770", 0, 0, 0, 0), 
                     (36, "Farmers and Foragers Food Truck", "Burlington", "75 Penny Lane, Burlington", "Canadian", "802-557-5074", 0, 0, 0, 0), 
                     (37, "Hen Of The Wood", "Burlington", "55 Cherry St, Burlington", "Canadian", "(802) 540-0534", 0, 0, 0, 0), 
                     (38, "Juniper Bar and Restaurant", "Burlington", "41 Cherry St (Hotel Vermont), Burlington", "Canadian", "(802) 651-5027", 1, 0, 0, 1), 
                     (39, "Bistro de Margot", "Burlington", "126 College St, Burlington", "French", "(802) 863-5200", 0, 0, 1, 1), 
                     (40, "Sherpa Kitchen", "Burlington", "119 College St, Burlington", "Indian", "(802) 881-0550", 1, 1, 1, 1), 
                     
                     (51, "CHOP Steakhouse & Bar", "Oakville", "3451 South Service Road West, Oakville", "Steakhouse", "(289) 881-7250", 1, 0, 0, 1), 
                     (52, "Dave & Buster's", "Oakville", "2021 Winston Park Dr e, Oakville", "American", "(289) 807-0300", 1, 0, 1, 1), 
                     (53, "East Side Mario's", "Oakville", "2035 Winston Park Dr, Oakville", "Italian", "(905) 829-3233", 1, 0, 0, 1), 
                     (54, "Symposium Cafe Restaurant", "Oakville", "1500 Upper Middle Rd W, Oakville", "Canadian", "(905) 847-2200", 1, 0, 0, 1), 
                     (55, "Ce Soir Brasserie + Bar", "Oakville", "134 Lakeshore Rd E, Oakville", "French", "(905) 844-0676", 1, 0, 0, 1), 
                     (56, "Harpers Landing", "Oakville", "481 Cornwall Road, Oakville", "American", "(905) 338-0707", 0, 0, 0, 0), 
                     (57, "Cucci Ristorante", "Oakville", "119 Jones Street, Oakville", "Italian", "(905) 469-1811", 0, 0, 0, 1), 
                     (58, "Beacon", "Oakville", "305 Lakeshore Rd E, Oakville", "American", "(905) 337-3777", 0, 0, 0, 0), 
                     (59, "Verace Restaurant", "Oakville", "312 Lakeshore Rd E, Oakville", "Italian", "(905) 337-0080", 0, 0, 0, 1), 
                     (60, "Trattoria Timone", "Oakville", "2091 Winston Park Drive, Oakville, ON L6H 6P5", "Italian", "(905) 842-2906", 0, 0, 0, 0), 
                     
                     (61, "The Keg Steakhouse + Bar", "Brampton", "46 Peel Centre Dr, Hudson'S Bay Bramalea City Centre, Brampton", "Steakhouse", "(289) 632-6322", 1, 0, 1, 1), 
                     (62, "Moxies", "Brampton", "56 Peel Centre Dr, Brampton", "American", "(905) 793-1633", 0, 1, 0, 1), 
                     (63, "Culinaria Restaurant", "Brampton", "5732 Kennedy Rd, Mississauga", "Canadian", "(905) 890-7330", 0, 0, 0, 1), 
                     (64, "Jack Astor's", "Brampton", "154 West Drive, Brampton", "Canadian", "(905) 457-5200", 0, 0, 0, 1), 
                     (65, "Montana's Trinity Common", "Brampton", "170 Great Lakes Dr, Brampton", "American", "(905) 789-6488", 0, 0, 0, 0), 
                     (66, "Turtle Jack's Muskoka Grill", "Brampton", "108 Courtney Park Dr., Mississauga", "Burgers", "(905) 362-0927", 0, 1, 0, 1), 
                     (67, "Montana's BBQ & Bar", "Brampton", "60 Courtneypark Dr E, Mississauga", "Canadian", "(905) 564-7391", 0, 0, 1, 1), 
                     (68, "Turtle Jacks Muskoka", "Brampton", "8295 Financial Dr, Brampton", "American", "(289) 368-2000", 0, 0, 0, 0), 
                     (69, "MISHREE Cocktails & Cuisine", "Brampton", "825 Britannia Rd W, Mississauga", "Indian", "(905) 690-6500", 1, 1, 0, 1), 
                     (70, "Beaumont Kitchen", "Brampton", "25 The West Mall, Etobicoke", "Canadian", "(416) 641-7327", 0, 0, 0, 0), 
                     
                     (71, "Capra's Kitchen", "Mississauga", "1834 LAKESHORE RD. W., Mississauga", "Italian", "(905) 916-1834", 0, 0, 1, 1), 
                     (72, "Rick's Good Eats", "Mississauga", "1-6660 Kennedy Road, Mississauga", "Burgers", "(905) 696-6966", 0, 0, 0, 0), 
                     (73, "Rogues Restaurant", "Mississauga", "1900 Dundas St W, Mississauga", "Canadian", "(905) 822-2670", 0, 0, 0, 0), 
                     (74, "A-One Catering", "Mississauga", " 7875 Tranmere Dr. Mississauga", "Indian", "(905) 677-9121", 0, 0, 0, 0), 
                     (75, "Leela's Roti", "Mississauga", "900 Rathburn Rd W, Mississauga", "Indian", "(905) 232-9070", 0, 1, 0, 1), 
                     (76, "The Hungry Dragon", "Mississauga", "1911 Ironoak Way, Oakville", "American", "(905) 822-1411", 0, 0, 0, 0), 
                     (77, "Guru Lakshmi", "Mississauga", "7070 Saint Barbara Blvd., Mississauga", "Indian", "(905) 795-2299", 0, 0, 0, 0), 
                     (78, "Colossus Greek Taverna", "Mississauga", "280 Lakeshore Rd. E., Port Credit", "Mediterranean", "(905) 271-2853", 0, 0, 0, 0), 
                     (79, "Szechuan Noodle Bowl", "Mississauga", "400 Dundas St E, Mississauga", "Chinese", "(905) 270-0068", 0, 0, 0, 0), 
                     (80, "Apricot Tree", "Mississauga", "1900 Dundas Street West, Mississauga", "European", "(905) 855-1470", 0, 0, 0, 0), 
                     
                     (81, "Frilu", "Markham", "7713 Yonge St, Thornhill", "Japanese", "(289) 597-8867", 0, 0, 1, 1), 
                     (82, "Tahchinbar", "Markham", "7181 Yonge St #16, Thornhill", "Iranian", "(905) 597-4554", 0, 0, 1, 1), 
                     (83, "Providential 9", "Markham", "CA Ontario, 8425 Woodbine Ave Unit A Markham", "Chinese", "(905) 305-1338", 0, 0, 0, 0), 
                     (84, "Skyview Fusion Cuisine", "Markham", "8261 Woodbine Ave #8, Markham", "Chinese", "(905) 944-9418", 1, 1, 0, 1), 
                     (85, "Zen Japanese Restaurant", "Markham", "7634 Woodbine Ave, Markham", "Japanese", "(905) 604-7211", 0, 0, 0, 0), 
                     (86, "Sam's Congee Delight", "Markham", "7354 Woodbine Ave, Markham", "Chinese", "(905) 479-1074", 0, 0, 0, 0), 
                     (87, "Diana's Oyster Bar & Grill", "Markham", "7501 Woodbine Ave, Markham", "Irish", "(905) 415-7792", 0, 1, 0, 1), 
                     (88, "Dum Pukht", "Markham", "323 Denison St, Markham", "Indian", "(905) 604-6401", 0, 1, 0, 0), 
                     (89, "QJD Peking Duck", "Markham", "7095 Woodbine Ave, Markham", "Chinese", "(905) 604-7798", 0, 0, 0, 0), 
                     (90, "Ding Tai Fung", "Markham", "3235 Hwy 7 #18B, Markham", "Chinese", "(905) 943-9880", 1, 0, 1, 1), 
                     
                     (91, "The Courtyard Casual Dining & Pub", "Vaughan", "1755 Pickering Pky, Pickering", "Canadian", "(905) 239-8714", 0, 0, 0, 0), 
                     (92, "Nascosto Ristorante", "Vaughan", "688 Chrislea Rd, Vaughan", "Italian", "(905) 265-1575", 0, 0, 0, 1), 
                     (93, "Earls Kitchen + Bar", "Vaughan", "40 Colossus Dr, Woodbridge", "American", "(905) 851-9600", 0, 0, 0, 0), 
                     (94, "Scaddabush Italian Kitchen & Bar", "Vaughan", "20 Colossus Drive, Vaughan", "Italian", "(905) 850-3565", 0, 0, 0, 0), 
                     (95, "Jack Astor's", "Vaughan", "10 Colossus Drive, Vaughan", "Canadian", "(905) 264-3790", 0, 0, 1, 1), 
                     (96, "Perla Oyster Bar & Grill", "Vaughan", "101-3901 Highway 7, Woodbridge", "Seafood", "(289) 657-0909", 0, 0, 0, 0), 
                     (97, "Mo Si Ristorante", "Vaughan", "3600 Langstaff Rd, Vaughan", "Italian", "(905) 850-1222", 1, 1, 1, 1), 
                     (98, "Moxies - Vaughan Colossus", "Vaughan", "Unit B - 30 Colossus Drive, Woodbridge", "American", "(905) 265-8090", 0, 0, 0, 0), 
                     (99, "PZA Restaurant & Bar", "Vaughan", "7777 Weston Road, Woodbridge", "Italian", "(905) 605-2335", 0, 0, 0, 0), 
                     (100, "3 Mariachis", "Vaughan", "9200 Weston Rd, Vaughan", "Mexican", "(905) 832-0606", 0, 1, 1, 0)
            """)
    
if __name__ == "__main__":
   conn = sqlite3.connect("project.db")
   c = conn.cursor()
   init_db(c)
      
   rs = c.execute("""SELECT * FROM Restaurant WHERE City = 'Mississauga'""")
   for r in rs.fetchall():
      print(r)
        
   conn.commit()
   conn.close()
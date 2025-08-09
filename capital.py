from tkinter import *
from tkinter import ttk
from tkinter import messagebox

country_capitals = {
    "Afghanistan": "Kabul",
    "Albania": "Tirana",
    "Algeria": "Algiers",
    "Andorra": "Andorra la Vella",
    "Angola": "Luanda",
    "Argentina": "Buenos Aires",
    "Armenia": "Yerevan",
    "Australia": "Canberra",
    "Austria": "Vienna",
    "Azerbaijan": "Baku",
    "Bahamas": "Nassau",
    "Bahrain": "Manama",
    "Bangladesh": "Dhaka",
    "Barbados": "Bridgetown",
    "Belarus": "Minsk",
    "Belgium": "Brussels",
    "Belize": "Belmopan",
    "Benin": "Porto-Novo",
    "Bhutan": "Thimphu",
    "Bolivia": "Sucre",
    "Bosnia and Herzegovina": "Sarajevo",
    "Botswana": "Gaborone",
    "Brazil": "Brasília",
    "Brunei": "Bandar Seri Begawan",
    "Bulgaria": "Sofia",
    "Burkina Faso": "Ouagadougou",
    "Burundi": "Gitega",
    "Cambodia": "Phnom Penh",
    "Cameroon": "Yaoundé",
    "Canada": "Ottawa",
    "Cape Verde": "Praia",
    "Central African Republic": "Bangui",
    "Chad": "N'Djamena",
    "Chile": "Santiago",
    "China": "Beijing",
    "Colombia": "Bogotá",
    "Comoros": "Moroni",
    "Costa Rica": "San José",
    "Croatia": "Zagreb",
    "Cuba": "Havana",
    "Cyprus": "Nicosia",
    "Czech Republic": "Prague",
    "Democratic Republic of the Congo": "Kinshasa",
    "Denmark": "Copenhagen",
    "Djibouti": "Djibouti",
    "Dominica": "Roseau",
    "Dominican Republic": "Santo Domingo",
    "Ecuador": "Quito",
    "Egypt": "Cairo",
    "El Salvador": "San Salvador",
    "Equatorial Guinea": "Malabo",
    "Eritrea": "Asmara",
    "Estonia": "Tallinn",
    "Eswatini": "Mbabane",
    "Ethiopia": "Addis Ababa",
    "Fiji": "Suva",
    "Finland": "Helsinki",
    "France": "Paris",
    "Gabon": "Libreville",
    "Gambia": "Banjul",
    "Georgia": "Tbilisi",
    "Germany": "Berlin",
    "Ghana": "Accra",
    "Greece": "Athens",
    "Grenada": "St. George's",
    "Guatemala": "Guatemala City",
    "Guinea": "Conakry",
    "Guinea-Bissau": "Bissau",
    "Guyana": "Georgetown",
    "Haiti": "Port-au-Prince",
    "Honduras": "Tegucigalpa",
    "Hungary": "Budapest",
    "Iceland": "Reykjavík",
    "India": "New Delhi",
    "Indonesia": "Jakarta",
    "Iran": "Tehran",
    "Iraq": "Baghdad",
    "Ireland": "Dublin",
    "Israel": "Jerusalem",
    "Italy": "Rome",
    "Ivory Coast": "Yamoussoukro",
    "Jamaica": "Kingston",
    "Japan": "Tokyo",
    "Jordan": "Amman",
    "Kazakhstan": "Astana",
    "Kenya": "Nairobi",
    "Kiribati": "Tarawa",
    "North Korea": "Pyongyang",
    "South Korea": "Seoul",
    "Kosovo": "Pristina",
    "Kuwait": "Kuwait City",
    "Kyrgyzstan": "Bishkek",
    "Laos": "Vientiane",
    "Latvia": "Riga",
    "Lebanon": "Beirut",
    "Lesotho": "Maseru",
    "Liberia": "Monrovia",
    "Libya": "Tripoli",
    "Liechtenstein": "Vaduz",
    "Lithuania": "Vilnius",
    "Luxembourg": "Luxembourg",
    "Madagascar": "Antananarivo",
    "Malawi": "Lilongwe",
    "Malaysia": "Kuala Lumpur",
    "Maldives": "Malé",
    "Mali": "Bamako",
    "Malta": "Valletta",
    "Marshall Islands": "Majuro",
    "Mauritania": "Nouakchott",
    "Mauritius": "Port Louis",
    "Mexico": "Mexico City",
    "Micronesia": "Palikir",
    "Moldova": "Chișinău",
    "Monaco": "Monaco",
    "Mongolia": "Ulaanbaatar",
    "Montenegro": "Podgorica",
    "Morocco": "Rabat",
    "Mozambique": "Maputo",
    "Myanmar": "Naypyidaw",
    "Namibia": "Windhoek",
    "Nauru": "Yaren",
    "Nepal": "Kathmandu",
    "Netherlands": "Amsterdam",
    "New Zealand": "Wellington",
    "Nicaragua": "Managua",
    "Niger": "Niamey",
    "Nigeria": "Abuja",
    "North Macedonia": "Skopje",
    "Norway": "Oslo",
    "Oman": "Muscat",
    "Pakistan": "Islamabad",
    "Palau": "Ngerulmud",
    "Panama": "Panama City",
    "Papua New Guinea": "Port Moresby",
    "Paraguay": "Asunción",
    "Peru": "Lima",
    "Philippines": "Manila",
    "Poland": "Warsaw",
    "Portugal": "Lisbon",
    "Qatar": "Doha",
    "Republic of the Congo": "Brazzaville",
    "Romania": "Bucharest",
    "Russia": "Moscow",
    "Rwanda": "Kigali",
    "Saint Kitts and Nevis": "Basseterre",
    "Saint Lucia": "Castries",
    "Saint Vincent and the Grenadines": "Kingstown",
    "Samoa": "Apia",
    "San Marino": "San Marino",
    "São Tomé and Príncipe": "São Tomé",
    "Saudi Arabia": "Riyadh",
    "Senegal": "Dakar",
    "Serbia": "Belgrade",
    "Seychelles": "Victoria",
    "Sierra Leone": "Freetown",
    "Singapore": "Singapore",
    "Slovakia": "Bratislava",
    "Slovenia": "Ljubljana",
    "Solomon Islands": "Honiara",
    "Somalia": "Mogadishu",
    "South Africa": "Pretoria",  # legislative capital
    "South Sudan": "Juba",
    "Spain": "Madrid",
    "Sri Lanka": "Sri Jayawardenepura Kotte",
    "Sudan": "Khartoum",
    "Suriname": "Paramaribo",
    "Sweden": "Stockholm",
    "Switzerland": "Bern",
    "Syria": "Damascus",
    "Taiwan": "Taipei",
    "Tajikistan": "Dushanbe",
    "Tanzania": "Dodoma",
    "Thailand": "Bangkok",
    "Timor-Leste": "Dili",
    "Togo": "Lomé",
    "Tonga": "Nukuʻalofa",
    "Trinidad and Tobago": "Port of Spain",
    "Tunisia": "Tunis",
    "Turkey": "Ankara",
    "Turkmenistan": "Ashgabat",
    "Tuvalu": "Funafuti",
    "Uganda": "Kampala",
    "Ukraine": "Kyiv",
    "United Arab Emirates": "Abu Dhabi",
    "United Kingdom": "London",
    "United States": "Washington, D.C.",
    "Uruguay": "Montevideo",
    "Uzbekistan": "Tashkent",
    "Vanuatu": "Port Vila",
    "Vatican City": "Vatican City",
    "Venezuela": "Caracas",
    "Vietnam": "Hanoi",
    "Yemen": "Sana'a",
    "Zambia": "Lusaka",
    "Zimbabwe": "Harare"
}

def open_first_window():
    global g1
    g1 = Toplevel(root)
    g1.geometry("300x130")
    g1.resizable(0, 0)
    g1.title("Game 1")
    label1 = Label(g1, text="Enter any capital of the world below", font="Calibre 10 bold")
    global entry1
    entry1 = ttk.Entry(g1, width=20)
    entry1.focus_set()
    btn3 = ttk.Button(g1, text="Submit", command=g1_fun)
    label1.pack()
    entry1.pack(pady=10)
    btn3.pack()

def g1_fun():
    user_capital = entry1.get().title().strip()
    if not user_capital:
        message = messagebox.showwarning(title="Missing entries", message="Be sure that you entered a capital in this entry")
        g1.destroy()
        return
    for country, capital_1 in country_capitals.items():
        if user_capital.lower() == capital_1.lower():
            message = messagebox.showinfo(title="Good Job", message=f"{user_capital} is definetely the capital of {country}")
            g1.destroy()
            return 
    message = messagebox.showinfo(title="Sorry you lose", message=f"{user_capital} isn't a capital for any country")
    g1.destroy()
    return

def open_second_window():
    global g2
    g2 = Toplevel(root)
    g2.title("Game 2")
    g2.resizable(0,0)
    g2.geometry("300x130")
    label2 = Label(g2, text="Enter a country and know its capital", font="Calibre 10 bold")
    btn4 = ttk.Button(g2, text="Submit", command=g2_fun)
    global entry2
    entry2 = ttk.Entry(g2, width=20)
    label2.pack()
    entry2.pack(pady=10)
    btn4.pack()

def g2_fun():
    user_country = entry2.get().title().strip()
    if not user_country:
        message = messagebox.showwarning(title="Missing entries", message="Be sure that you entered a country in this entry")
        g2.destroy()
        return
    for country, capital in country_capitals.items():
        if user_country.lower() == country.lower():
            message = messagebox.showinfo(title="Correct", message=f"{user_country} is a country whose capital is {capital}")
            g2.destroy()
            return
    sad_message = messagebox.showinfo(title="Sorry you lose", message=f"No, {user_country} is not a country")
    g2.destroy()
    return     

# start
root = Tk()
root.geometry("200x130")
root.resizable(0, 0)
root.title("Home screen")

label = Label(root, text="Capitals of the world", font="Calibre 10 bold")
label.pack()

btn1 = ttk.Button(root, text="Game 1", command=open_first_window)
btn1.pack(pady=10)

btn2 = ttk.Button(root, text="Game 2", command=open_second_window)
btn2.pack(pady=10)

root.mainloop()
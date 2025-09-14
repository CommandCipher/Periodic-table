print("Welcome to periodic table helper!")
print("Below are all the 118 elements in periodic table.")

username = input("What is your name? ")

print("Elements are in the following form:-\n(Name)(Symbol)(Atomic Number)")
print("_____________________________")

print("Hydrogen(H)(1)\nHelium(He)(2)\nLithium(Li)(3)\nBeryllium(Be)(4)\nBoron(B)(5)\nCarbon(C)(6)")
print("Nitrogen(N)(7)\nOxygen(O)(8)\nFluorine(F)(9)\nNeon(Ne)(10)\nSodium(Na)(11)\nMagnesium(Mg)(12)")
print("Aluminium(Al)(13)\nSilicon(Si)(14)\nPhosphorus(P)(15)\nSulfur(S)(16)\nChlorine(Cl)(17)")
print("Argon(Ar)(18)\nPotassium(K)(19)\nCalcium(Ca)(20)\nScandium(Sc)(21)\nTitanium(Ti)(22)")
print("Vanadium(V)(23)\nChromium(Cr)(24)\nManganese(Mn)(25)\nIron(Fe)(26)\nCobalt(Co)(27)\nNickel(Ni)(28)")
print("Copper(Cu)(29)\nZinc(Zn)(30)\nGallium(Ga)(31)\nGermanium(Ge)(32)\nArsenic(As)(33)\nSelenium(Se)(34)")
print("Bromine(Br)(35)\nKrypton(Kr)(36)\nRubidium(Rb)(37)\nStrontium(Sr)(38)\nYttrium(Y)(39)")
print("Zirconium(Zr)(40)\nNiobium(Nb)(41)\nMolybdenum(Mo)(42)\nTechnetium(Tc)(43)\nRuthenium(Ru)(44)")
print("Rhodium(Rh)(45)\nPalladium(Pd)(46)\nSilver(Ag)(47)\nCadmium(Cd)(48)\nIndium(In)(49)\nTin(Sn)(50)")
print("Antimony(Sb)(51)\nTellurium(Te)(52)\nIodine(I)(53)\nXenon(Xe)(54)\nCesium(Cs)(55)\nBarium(Ba)(56)")
print("Lanthanum(La)(57)\nCerium(Ce)(58)\nPraseodymium(Pr)(59)\nNeodymium(Nd)(60)\nPromethium(Pm)(61)")
print("Samarium(Sm)(62)\nEuropium(Eu)(63)\nGadolinium(Gd)(64)\nTerbium(Tb)(65)\nDysprosium(Dy)(66)")
print("Holmium(Ho)(67)\nErbium(Er)(68)\nThulium(Tm)(69)\nYtterbium(Yb)(70)\nLutetium(Lu)(71)\nHafnium(Hf)(72)")
print("Tantalum(Ta)(73)\nTungsten(W)(74)\nRhenium(Re)(75)\nOsmium(Os)(76)\nIridium(Ir)(77)\nPlatinum(Pt)(78)")
print("Gold(Au)(79)\nMercury(Hg)(80)\nThallium(Tl)(81)\nLead(Pb)(82)\nBismuth(Bi)(83)\nPolonium(Po)(84)")
print("Astatine(At)(85)\nRadon(Rn)(86)\nFrancium(Fr)(87)\nRadium(Ra)(88)\nActinium(Ac)(89)\nThorium(Th)(90)")
print("Protactinium(Pa)(91)\nUranium(U)(92)\nNeptunium(Np)(93)\nPlutonium(Pu)(94)\nAmericium(Am)(95)")
print("Curium(Cm)(96)\nBerkelium(Bk)(97)\nCalifornium(Cf)(98)\nEinsteinium(Es)(99)\nFermium(Fm)(100)")
print("Mendelevium(Md)(101)\nNobelium(No)(102)\nLawrencium(Lr)(103)\nRutherfordium(Rf)(104)\nDubnium(Db)(105)")
print("Seaborgium(Sg)(106)\nBohrium(Bh)(107)\nHassium(Hs)(108)\nMeitnerium(Mt)(109)\nDarmstadtium(Ds)(110)")
print("Roentgenium(Rg)(111)\nCopernicium(Cn)(112)\nNihonium(Nh)(113)\nFlerovium(Fl)(114)\nMoscovium(Mc)(115)")
print("Livermorium(Lv)(116)\nTennessine(Ts)(117)\nOganesson(Og)(118)")

a_no = int(input("\nInput the atomic number of the element about which you want more info:- "))

if a_no == 1:

    print("You chose hydrogen.")

    print("\nAPPEARANCE:-\nA colourless, odourless gas. It has the lowest density of all gases.")

    print("\nUSES:-\nSome see hydrogen gas as the clean fuel of the future – generated from water and returning to water\n "
          "when it is oxidised. Hydrogen-powered fuel cells are increasingly being seen as ‘pollution-free’ sources of\n"
          "energy and are now being used in some buses and cars. Hydrogen also has many other uses. In the chemical\n"
          "industry it is used to make ammonia for agricultural fertiliser (the Haber process) and cyclohexane and\n"
          "methanol, which are intermediates in the production of plastics and pharmaceuticals. It is also used to\n"
          "remove sulfur from fuels during the oil-refining process. Large quantities of hydrogen are used to\n"
          "hydrogenate oils to form fats, for example to make margarine. In the glass industry hydrogen is used as a\n"
          "protective atmosphere for making flat glass sheets. In the electronics industry it is used as a flushing gas\n"
          "during the manufacture of silicon chips. The low density of hydrogen made it a natural choice for one of its\n"
          "first practical uses – filling balloons and airships. However, it reacts vigorously with oxygen\n"
          " (to form water) and its future in filling airships ended when the Hindenburg airship caught fire.\n")

    print("\nBIOLOGICAL ROLE:-\nHydrogen is an essential element for life. It is present in water and in almost all the\n"
          "molecules in living things. However, hydrogen itself does not play a particularly active role. It remains\n"
          "bonded to carbon and oxygen atoms, while the chemistry of life takes place at the more active sites involving,\n"
          " for example, oxygen, nitrogen and phosphorus.\n")

    print("\nNATURAL ABUNDANCE:-\nHydrogen is easily the most abundant element in the universe. It is found in the sun\n"
          "and most of the stars, and the planet Jupiter is composed mostly of hydrogen. On Earth, hydrogen is found in\n"
          "the greatest quantities as water. It is present as a gas in the atmosphere only in tiny amounts– less than\n"
          "1 part per million by volume. Any hydrogen that does enter the atmosphere quickly escapes the Earth’s gravity\n"
          " into outer space. Most hydrogen is produced by heating natural gas with steam to form syngas (a mixture of\n"
          "hydrogen and carbon monoxide). The syngas is separated to give\nhydrogen. Hydrogen can also be produced by\n"
          "the electrolysis of water.\n")

elif a_no == 2:

      print("\nYou chose helium.")

      print("\nAPPEARANCE:-\nA colourless, odourless gas that is totally unreactive.\n")

      print("\nUSES:-\nHelium is used as a cooling medium for the Large Hadron Collider (LHC), and the superconducting"
            "\nmagnets in MRI scanners and NMR spectrometers. It is also used to keep satellite instruments cool and was"
            "\nused to cool the liquid oxygen and hydrogen that powered the Apollo space vehicles. Because of its low "
            "\ndensity helium is often used to fill decorative balloons, weather balloons and airships. Hydrogen was "
            "\nonce used to fill balloons but it is dangerously reactive. Because it is very unreactive, helium is used "
            "\nto provide an inert protective atmosphere for making fibre optics and semiconductors, and for arc welding."
            "\nHelium is also used to detect leaks, such as in car air-conditioning systems, and because it diffuses "
            "\nquickly it is used to inflate car airbags after impact. A mixture of 80% helium and 20% oxygen is used as"
            "\nan artificial atmosphere for deep-sea divers and others working under pressurised conditions. Helium-neon"
            "\n gas lasers are used to scan barcodes in supermarket checkouts. A new use for helium is a helium-ion "
            "\nmicroscope that gives better image resolution than a scanning electron microscope.\n")

      print("\nBIOLOGICAL ROLE:-\nHelium has no known biological role. It is non-toxic.\n")

      print("\nNATURAL ABUNDANCE:-\nAfter hydrogen, helium is the second most abundant element in the universe. It is "
            "\npresent in all stars. It was, and is still being, formed from alpha-particle decay of radioactive "
            "\nelements in the Earth. Some of the helium formed escapes into the atmosphere, which contains about 5 "
            "\nparts per million by volume. This is a dynamic balance, with the low-density helium continually escaping"
            "\nto outer space. It is uneconomical to extract helium from the air. The major source is natural gas, which"
            "\ncan contain up to 7% helium.\n")

elif a_no == 3:

      print("You chose lithium.")

      print("\nAPPEARANCE:-\nA soft, silvery metal. It has the lowest density of all metals. It reacts vigorously with "
            "\nwater.")

      print("\nUSES:-\nThe most important use of lithium is in rechargeable batteries for mobile phones, laptops, "
            "\ndigital cameras and electric vehicles. Lithium is also used in some non-rechargeable batteries for things"
            "\nlike heart pacemakers, toys and clocks. Lithium metal is made into alloys with aluminium and magnesium, "
            "\nimproving their strength and making them lighter. A magnesium-lithium alloy is used for armour plating. "
            "\nAluminium-lithium alloys are used in aircraft, bicycle frames and high-speed trains. Lithium oxide is "
            "\nused in special glasses and glass ceramics. Lithium chloride is one of the most hygroscopic materials "
            "\nknown, and is used in air conditioning and industrial drying systems (as is lithium bromide). Lithium "
            "\nstearate is used as an all-purpose and high-temperature lubricant. Lithium carbonate is used in drugs to "
            "\ntreat manic depression, although its action on the brain is still not fully understood. Lithium hydride "
            "\nis used as a means of storing hydrogen for use as a fuel.")

      print("\nBIOLOGICAL ROLE:-\nLithium has no known biological role. It is toxic, except in very small doses.")

      print("\nNATURAL ABUNDANCE:-\nLithium does not occur as the metal in nature, but is found combined in small "
            "\namounts in nearly all igneous rocks and in the waters of many mineral springs. Spodumene, petalite, "
            "\nlepidolite, and amblygonite are the more important minerals containing lithium. Most lithium is currently"
            "\nproduced in Chile, from brines that yield lithium carbonate when treated with sodium carbonate. The metal"
            "\nis produced by the electrolysis of molten lithium chloride and potassium chloride.")

elif a_no == 4:

      print("You chose beryllium.")

      print("\nAPPEARANCE:-\nBeryllium is a silvery-white metal. It is relatively soft and has a low density.")

      print("\nUSES:-\nBeryllium is used in alloys with copper or nickel to make gyroscopes, springs, electrical "
            "\ncontacts, spot-welding electrodes and non-sparking tools. Mixing beryllium with these metals increases"
            "\ntheir electrical and thermal conductivity. Other beryllium alloys are used as structural materials for "
            "\nhigh-speed aircraft, missiles, spacecraft and communication satellites. Beryllium is relatively "
            "\ntransparent to X-rays so ultra-thin beryllium foil is finding use in X-ray lithography. Beryllium is also"
            "\n used in nuclear reactors as a reflector or moderator of neutrons. The oxide has a very high melting "
            "\npoint making it useful in nuclear work as well as having ceramic applications.")

      print("\nBIOLOGICAL ROLE:-\nBeryllium and its compounds are toxic and carcinogenic. If beryllium dust or fumes are"
            "\n inhaled, it can lead to an incurable inflammation of the lungs called berylliosis.")

      print("NATURAL ABUNDANCE:-\nBeryllium is found in about 30 different mineral species. The most important are beryl"
            "\n(beryllium aluminium silicate) and bertrandite (beryllium silicate). Emerald and aquamarine are precious "
            "\nforms of beryl. The metal is usually prepared by reducing beryllium fluoride with magnesium metal.")

elif a_no == 5:

      print("You chose boron.")

      print("\nAPPEARANCE:-\nPure boron is a dark amorphous powder.")

      print("\nUSES:-\nAmorphous boron is used as a rocket fuel igniter and in pyrotechnic flares. It gives the flares a"
            "\ndistinctive green colour. The most important compounds of boron are boric (or boracic) acid, borax "
            "\n(sodium borate) and boric oxide. These can be found in eye drops, mild antiseptics, washing powders and "
            "\ntile glazes. Borax used to be used to make bleach and as a food preservative. Boric oxide is also "
            "\ncommonly used in the manufacture of borosilicate glass (Pyrex). It makes the glass tough and heat "
            "\nresistant. Fibreglass textiles and insulation are made from borosilcate glass. Sodium octaborate is a "
            "\nflame retardant. The isotope boron-10 is good at absorbing neutrons. This means it can be used to "
            "\nregulate nuclear reactors. It also has a role in instruments used to detect neutrons.")

      print("\nBIOLOGICAL ROLE:-\nBoron is essential for the cell walls of plants. It is not considered poisonous to "
            "\nanimals, but in higher doses it can upset the body’s metabolism. We take in about 2 milligrams of boron "
            "\neach day from our food, and about 60 grams in a lifetime. Some boron compounds are being studied as a "
            "\npossible treatment for brain tumours.")

      print("NATURAL ABUNDANCE:-\nHigh-purity boron is prepared by reducing boron trichloride or tribromide with "
            "\nhydrogen, on electrically heated filaments. Impure, or amorphous, boron can be prepared by heating the "
            "\ntrioxide with magnesium powder.")

elif a_no == 6:

      print("\nYou chose carbon.")

      print("\nAPPEARANCE:-\nThere are a number of pure forms of this element including graphite, diamond, fullerenes "
            "\nand graphene. Diamond is a colourless, transparent, crystalline solid and the hardest known material. "
            "\nGraphite is black and shiny but soft. The nano-forms, fullerenes and graphene, appear as black or dark "
            "\nbrown, soot-like powders.")

      print("\nUSES:-\nCarbon is unique among the elements in its ability to form strongly bonded chains, sealed off by"
            "\nhydrogen atoms. These hydrocarbons, extracted naturally as fossil fuels (coal, oil and natural gas), are"
            "\nmostly used as fuels. A small but important fraction is used as a feedstock for the petrochemical "
            "\nindustries producing polymers, fibres, paints, solvents and plastics etc. Impure carbon in the form of"
            "\ncharcoal (from wood) and coke (from coal) is used in metal smelting. It is particularly important in the"
            "\niron and steel industries. Graphite is used in pencils, to make brushes in electric motors and in furnace"
            "\nlinings. Activated charcoal is used for purification and filtration. It is found in respirators and "
            "\nkitchen extractor hoods. Carbon fibre is finding many uses as a very strong, yet lightweight, material. "
            "\nIt is currently used in tennis rackets, skis, fishing rods, rockets and aeroplanes. Industrial diamonds"
            "\nare used for cutting rocks and drilling. Diamond films are used to protect surfaces such as razor blades."
            "\nThe more recent discovery of carbon nanotubes, other fullerenes and atom-thin sheets of graphene has"
            "\nrevolutionised hardware developments in the electronics industry and in nanotechnology generally. 150 "
            "\nyears ago the natural concentration of carbon dioxide in the Earth’s atmosphere was 280 ppm. In 2013, as"
            "\na result of combusting fossil fuels with oxygen, there was 390 ppm. Atmospheric carbon dioxide allows "
            "\nvisible light in but prevents some infrared escaping (the natural greenhouse effect). This keeps the "
            "\nEarth warm enough to sustain life. However, an enhanced greenhouse effect is underway, due to a human-"
            "\ninduced rise in atmospheric carbon dioxide. This is affecting living things as our climate changes.")

      print("\nBIOLOGICAL ROLE:-\nCarbon is essential to life. This is because it is able to form a huge variety of"
            "\nchains of different lengths. It was once thought that the carbon-based molecules of life could only be "
            "\nobtained from living things. They were thought to contain a ‘spark of life’. However, in 1828, urea was "
            "\nsynthesised from inorganic reagents and the branches of organic and inorganic chemistry were united."
            "\nLiving things get almost all their carbon from carbon dioxide, either from the atmosphere or dissolved in"
            "\nwater. Photosynthesis by green plants and photosynthetic plankton uses energy from the sun to split water"
            "\ninto oxygen and hydrogen. The oxygen is released to the atmosphere, fresh water and seas, and the "
            "\nhydrogen joins with carbon dioxide to produce carbohydrates. Some of the carbohydrates are used, along "
            "\nwith nitrogen, phosphorus and other elements, to form the other monomer molecules of life. These include "
            "\nbases and sugars for RNA and DNA, and amino acids for proteins. Living things that do not photosynthesis"
            "\nhave to rely on consuming other living things for their source of carbon molecules. Their digestive "
            "\nsystems break carbohydrates into monomers that they can use to build their own cellular structures. "
            "\nRespiration provides the energy needed for these reactions. In respiration oxygen rejoins carbohydrates, "
            "\nto form carbon dioxide and water again. The energy released in this reaction is made available for the "
            "\ncells.")

      print("\nNATURAL ABUNDANCE:-\nCarbon is found in the sun and other stars, formed from the debris of a previous "
            "\nsupernova. It is built up by nuclear fusion in bigger stars. It is present in the atmospheres of many "
            "\nplanets, usually as carbon dioxide. On Earth, the concentration of carbon dioxide in the atmosphere is "
            "\ncurrently 390 ppm and rising. Graphite is found naturally in many locations. Diamond is found in the form"
            "\nof microscopic crystals in some meteorites. Natural diamonds are found in the mineral kimberlite, sources"
            "\nof which are in Russia, Botswana, DR Congo, Canada and South Africa. In combination, carbon is found in "
            "\nall living things. It is also found in fossilised remains in the form of hydrocarbons (natural gas, crude"
            "\noil, oil shales, coal etc) and carbonates (chalk, limestone, dolomite etc).")

elif a_no == 7:

      print("\nYou chose nitrogen.")

      print("\nAPPEARANCE:-\nA colourless, odourless gas.")


      print("\nUSES:-\nNitrogen is important to the chemical industry. It is used to make fertilisers, nitric acid, "
            "\nnylon, dyes and explosives. To make these products, nitrogen must first be reacted with hydrogen to "
            "\nproduce ammonia. This is done by the Haber process. 150 million tonnes of ammonia are produced in this "
            "\nway every year. Nitrogen gas is also used to provide an unreactive atmosphere. It is used in this way to "
            "\npreserve foods, and in the electronics industry during the production of transistors and diodes. Large "
            "\nquantities of nitrogen are used in annealing stainless steel and other steel mill products. Annealing is "
            "\na heat treatment that makes steel easier to work. Liquid nitrogen is often used as a refrigerant. It is "
            "\nused for storing sperm, eggs and other cells for medical research and reproductive technology. It is also "
            "\nused to rapidly freeze foods, helping them to maintain moisture, colour, flavour and texture.")

      print("\nBIOLOGICAL ROLE:-\nNitrogen is cycled naturally by living organisms through the ‘nitrogen cycle’. It is "
            "\ntaken up by green plants and algae as nitrates, and used to build up the bases needed to construct DNA, "
            "\nRNA and all amino acids. Amino acids are the building blocks of proteins. Animals obtain their nitrogen "
            "\nby consuming other living things. They digest the proteins and DNA into their constituent bases and amino "
            "\nacids, reforming them for their own use. Microbes in the soil convert the nitrogen compounds back to "
            "\nnitrates for the plants to re-use. The nitrate supply is also replenished by nitrogen-fixing bacteria "
            "\nthat ‘fix’ nitrogen directly from the atmosphere. Crop yields can be greatly increased by adding chemical "
            "\nfertilisers to the soil, manufactured from ammonia. If used carelessly the fertiliser can leach out of "
            "\nthe soil into rivers and lakes, causing algae to grow rapidly. This can block out light preventing "
            "\nphotosynthesis. The dissolved oxygen soon gets used up and the river or lake dies.")

      print("\nNATURAL ABUNDANCE:-\nNitrogen makes up 78% of the air, by volume. It is obtained by the distillation of "
            "\nliquid air. Around 45 million tonnes are extracted each year. It is found, as compounds, in all living "
            "\nthings and hence also in coal and other fossil fuels.")

elif a_no == 8:

      print("\nYou chose oxygen.")

      print("\nAPPEARANCE:-\nA colourless, odourless gas.")

      print("\nUSES:-\nThe greatest commercial use of oxygen gas is in the steel industry. Large quantities are also "
            "\nused in the manufacture of a wide range of chemicals including nitric acid and hydrogen peroxide. It is "
            "\nalso used to make epoxyethane (ethylene oxide), used as antifreeze and to make polyester, and chloroethene, "
            "\nthe precursor to PVC. Oxygen gas is used for oxy-acetylene welding and cutting of metals. A growing use "
            "\nis in the treatment of sewage and of effluent from industry.")

      print("\nBIOLOGICAL ROLE:_\nOxygen first appeared in the Earth’s atmosphere around 2 billion years ago, "
            "\naccumulating from the photosynthesis of blue-green algae. Photosynthesis uses energy from the sun to "
            "\nsplit water into oxygen and hydrogen. The oxygen passes into the atmosphere and the hydrogen joins with "
            "\ncarbon dioxide to produce biomass. When living things need energy they take in oxygen for respiration. "
            "\nThe oxygen returns to the atmosphere in the form of carbon dioxide. Oxygen gas is fairly soluble in water,"
            "\nwhich makes aerobic life in rivers, lakes and oceans possible.")

      print("\nNATURAL ABUNDANCE:-\nOxygen makes up 21% of the atmosphere by volume. This is halfway between 17% (below "
            "\nwhich breathing for unacclimatised people becomes difficult) and 25% (above which many organic compounds "
            "\nare highly flammable). The element and its compounds make up 49.2% by mass of the Earth’s crust, and "
            "\nabout two-thirds of the human body. There are two key methods used to obtain oxygen gas. The first is by "
            "\nthe distillation of liquid air. The second is to pass clean, dry air through a zeolite that absorbs "
            "\nnitrogen and leaves oxygen. A newer method, which gives oxygen of a higher purity, is to pass air over a "
            "\npartially permeable ceramic membrane. In the laboratory it can be prepared by the electrolysis of water "
            "\nor by adding a manganese(IV) oxide catalyst to aqueous hydrogen peroxide.")

elif a_no == 9:

      print("\nYou chose Flourine.")

      print("\nAPPEARANCE:-\nA very pale yellow-green, dangerously reactive gas. It is the most reactive of all the "
            "\nelements and quickly attacks all metals. Steel wool bursts into flames when exposed to fluorine.")

      print("\nUSES:-\nThere was no commercial production of fluorine until the Second World War, when the development of the "
            "\natom bomb, and other nuclear energy projects, made it necessary to produce large quantities. Before this, "
            "\nfluorine salts, known as fluorides, were for a long time used in welding and for frosting glass. The "
            "\nelement is used to make uranium hexafluoride, needed by the nuclear power industry to separate uranium "
            "\nisotopes. It is also used to make sulfur hexafluoride, the insulating gas for high-power electricity "
            "\ntransformers. In fact, fluorine is used in many fluorochemicals, including solvents and high-temperature "
            "\nplastics, such as Teflon (polytetrafluoroethene), PTFE). Teflon is well known for its non-stick "
            "\nproperties and is used in frying pans. It is also used for cable insulation, for plumber’s tape and as "
            "\nthe basis of Gore-Tex® (used in waterproof shoes and clothing). Hydrofluoric acid is used for etching the "
            "\nglass of light bulbs and in similar applications. CFCs (chloro-fluoro-carbons) were once used as aerosol "
            "\npropellants, refrigerants and for ‘blowing’ expanded polystyrene. However, their inertness meant that, "
            "\nonce in the atmosphere, they diffused into the stratosphere and destroyed the Earth’s ozone layer. They "
            "\nare now banned.")

      print("\nBIOLOGICAL ROLE:-\nFluoride is an essential ion for animals, strengthening teeth and bones. It is added "
            "\nto drinking water in some areas. The presence of fluorides below 2 parts per million in drinking water is "
            "\nbelieved to prevent dental cavities. However, above this concentration it may cause children’s tooth "
            "\nenamel to become mottled. Fluoride is also added to toothpaste. The average human body contains about 3 "
            "\nmilligrams of fluoride. Too much fluoride is toxic. Elemental fluorine is highly toxic.")

      print("\nNATURAL ABUNDANCE:-\nThe most common fluorine minerals are fluorite, fluorspar and cryolite, but it is "
            "\nalso rather widely distributed in other minerals. It is the 13th most common element in the Earth’s crust."
            "\nFluorine is made by the electrolysis of a solution of potassium hydrogendifluoride (KHF2) in anhydrous "
            "\nhydrofluoric acid.")

elif a_no == 10:

      print("\nYou chose neon.")

      print("\nAPPEARANCE:-\nA colourless, odourless gas. Neon will not react with any other substance.")

      print("\nUSES:-\nThe largest use of neon is in making the ubiquitous ‘neon signs’ for advertising. In a vacuum "
            "\ndischarge tube neon glows a reddish orange colour. Only the red signs actually contain pure neon. Others "
            "\ncontain different gases to give different colours. Neon is also used to make high-voltage indicators and"
            "\nswitching gear, lightning arresters, diving equipment and lasers. Liquid neon is an important cryogenic "
            "\nrefrigerant. It has over 40 times more refrigerating capacity per unit volume than liquid helium, and "
            "\nmore than 3 times that of liquid hydrogen.")

      print("\nBIOLOGICAL ROLE:-\nNeon has no known biological role. It is non-toxic.")

      print("\nNATURAL ABUNDANCE:-\nNeon is the fifth most abundant element in the universe. However, it is present in "
            "\nthe Earth’s atmosphere at a concentration of just 18 parts per million. It is extracted by fractional "
            "\ndistillation of liquid air. This gives a fraction that contains both helium and neon. The helium is "
            "\nremoved from the mixture with activated charcoal.")



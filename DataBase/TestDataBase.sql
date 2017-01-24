CREATE TABLE Test(
	Question_id 		int UNIQUE Primary key,
    Question_type		Varchar(25),
	Question_Catagory	Varchar(35),
    Question 			varchar(250),
    Anwser1				varchar(200),
    Anwser2				varchar(200),
    Anwser3				varchar(200),
    Correct_anwser		varchar(200)
);







INSERT INTO Test(Question_ID, Question_type, Question_Catagory, Question, Anwser1, Anwser2, Anwser3, correct_anwser)
VALUES 

(16, 'MC', 'Geography', 'Wat is het belangrijkste vervoersmiddel in Rotterdam?', 'A. Metro', 'B. Auto', 'C. Fiets', 'A'),
(17, 'MC', 'Geography',  'De haven van Rotterdam is grootste haven van Nederland.', 'A. Waar', 'B. Niet Waar', NULL, 'A'),
(18, 'MC', 'Geography', 'Hoe wordt Rotterdam ook wel genoemd', 'A. Stad der wonderen', 'B. Stad der steden', 'C. Haven stad', 'C'),
(19, 'MC', 'Geography', 'In welke provincie ligt Rotterdam?', 'A. Noord-Holland', 'B. Zuid-Holland', 'C. Noord-Holland', 'B'),
(20, 'MC', 'Geography', 'Rotterdam is de hoofdstad van Zuid-Holland.', 'A. Waar', 'B. Niet Waar', NULL, 'B'),
(21, 'MC', 'Geography', 'Hoeveel regen valt er gemiddeld per jaar in Rotterdam?', 'A. 760 tot 780mm', 'B. 780 tot 800mm', 'C. 800 tot 820mm', 'C'),
(22, 'MC', 'Geography', 'Welke brug in Rotterdam heeft de volgende bijnaam: De zwaan.', 'A. De Willemsbrug', 'B. De Erasmusbrug', 'C. De van Briennenoordbrug', 'B'),
(23, 'MC', 'Geography', 'Rotterdam is de hoofdstad van Nederland.', 'A. Waar', 'B. Niet Waar', NULL, 'B'),
(24, 'MC', 'Geography', 'Wat is het oudste gebouw van Rotterdam?', 'A. Kerktoren Hillegondakerk', 'B. St. Laurenskerk', 'C. Stadhuis van Rotterdam', 'A'),
(25, 'MC', 'Geography', 'Rotterdam is de grootste stad van Nederland.', 'A. Waar', 'B. Niet Waar', NULL, 'A'),
(26, 'MC', 'Geography', 'Hoeveel mensen maken dagelijks gebruik van het openbaar vervoer in Rotterdam?', 'A. 800.00', 'B. 900.00', 'C. 1.000.000', 'C'),
(27, 'MC', 'Geography', 'Wat is de oudste brug van Rotterdam?', 'A. De Willemsbrug', 'B. De Koninginnebrug', 'C. De van Briennenoordbrug', 'B'),
(28, 'MC', 'Geography', 'Hoe heet de grootste rivier waar Rotterdam aan grenst', 'A. De Maas', 'B. De Rijn', 'C. De Waal', 'A'),
(29, 'MC', 'Geography', 'Hoeveel woningen zijn er ongeveer in Rotterdam?', 'A. 150.000', 'B. 300.000', 'C. 450.000', 'B'),
(30, 'MC', 'History', 'Wanneer is diergaarde Blijdorp geopend?', 'A. 1855', 'B. 1975', 'C. 1915', 'A'),
(31, 'MC', 'History', 'Waar dankt Rotterdam zijn naam aan?', 'A. Kooplieden hadden dit vroeger bedacht', 'B. Aan de rivier de rotte', 'C. Er was een dam aangelegd in de Maas', 'B'), 
(32, 'MC', 'History', 'Waar stond vroeger de wijk Katendrecht om bekend?', 'A. De beste bakker van de stad was daar gevestigd', 'B. De prostituees', 'C. De oudste beschermde boom van de stad staat door', 'B'), 
(33, 'MC', 'History', 'Wie is de nachtburgemeester van Rotterdam?', 'A. Ahmed Aboutaleb', 'B. Jules Deelder', 'C. Willer Alexander', 'B'),
(34, 'MC', 'History', 'In welk jaar heeft Rotterdam stadsrechten gekregen?', 'A. 1250', 'B. 1340', 'C. 1590', 'B'),
(35, 'MC', 'History', 'Wat is het enigste overgebleven middeleeuws gebouw in de binnenstad van Rotterdam?', 'A. De oude haven', 'B. VOC magazijn', 'C. St. Laurenskerk', 'C'),
(36, 'MC', 'History', 'Wat was tijdens de Wereldoorlog de enige weg naar het centrum die de Duitsers probeerden te bereiken?', 'A. De nieuwe Binnenweg', 'B. Maasbrug', 'C. Koninginnenbrug', 'B'), 
(37, 'MC', 'History', 'Wat is de officiÃ«le naam van de koopgoot?', 'A. De ondergrondse winkelstraat', 'B. Beurstraverse', 'C. Gewoon de koopgoot', 'B'),
(38, 'MC', 'History', 'Na 1872 is de stad Rotterdam snel groot geworden, Pieter Caland had een plan om Rotterdam met de zee te verbinden. Hoe noemde hij die verbinding?', 'A. De Nieuwe Waterweg', 'B. De Maas zeeverbinding', 'C. Het Nieuwe Water kanaal', 'A'),
(39, 'MC', 'History', 'Door welke architect(en) is de Euromast ontworpen?', 'A. Maaskant', 'B. Brinkman en van der Vlugt', 'C. Koolhaas', 'A'), 
(40, 'MC', 'History', 'Rotterdam was tot 1870 een opslag haven, welke producten werden er onder ander opgeslagen?', 'A. Suiker', 'B. Wol', 'C. Cacao', 'A'),
(41, 'MC', 'History', 'Welk gebouw (gebouwd in 1957) stond symbool voor de wederopbouw van de stad?', 'A. De Bijenkorf', 'B. De Kubuswoningen', 'C. The Red Apple', 'A'),
(42, 'MC', 'History', 'Hoeveel joden woonden er in Rotterdam voor de Tweede Wereldoorlog?', 'A. Ca. 5000', 'B. Ca. 8000', 'C. Ca. 12000', 'B'),
(43, 'MC', 'History', 'Hoe heette de haven van Rotterdam oorspronkelijk tijdens zijn ontstaan?', 'A. Waalhaven', 'B. De maashaven', 'C. Europoort', 'A'), 
(44, 'MC', 'History', 'Was de eerste metrolijn in Nederland in Rotterdam geopend?', 'A. Waar', 'B. Niet Waar', NULL, 'A'),
(61, 'MC', 'Entertainment', 'Welk van de volgende restaurantboten in Rotterdam bestaat niet?', 'A. De Zwanenboot', 'B. De Pannenkoekenboot', 'C. De Berenboot', 'A'),
(62, 'MC', 'Entertainment', 'Welke van de volgende Pathé bioscopen is niet in Rotterdam?', 'A. De Kuip', 'B. De Kroon', 'C. Schouwburgplein', 'B'),
(63, 'MC', 'Entertainment', 'Voor welkvervoer middel is er geen tour beschikbaar in Rotterdam?', 'A. Segway', 'B. Boot', 'C. Auto', 'C'),
(64, 'MC', 'Entertainment', 'In welke bioscoop vindt het Wildlife film festival plaats?', 'A. Cinerama', 'B. Pathé de Kuip', 'C. Pathé Schouwburgplein', 'A'),
(65, 'MC', 'Entertainment', 'Voor welk Museum staat het monument van Zadkine genaamd “de verwoeste stad”?', 'A. Havenmuseum', 'B. Mariniersmuseum', 'C. Maritiem museum', 'C'),
(66, 'MC', 'Entertainment', 'Waar kan je niet terecht om te gaan zwemmen?', 'A. Hoek van Holland', 'B. Euromast park', 'C. Plaswijkpark', 'B'),
(67, 'MC', 'Entertainment', 'Waar geeft Rotterdam Tours onder andere rondleidingen?', 'A. De Euromast', 'B. Museumplein', 'C. De Markthal', 'C'),
(82, 'MC', 'Entertainment', 'Welk van de volgende bioscopen is het oudst', 'A. Cinerama', 'B. Pathé de kuip', 'C. Lantaren-venster', 'C'),
(83, 'MC', 'Entertainment', 'Hoe heet de culturele en culinaire ontdekkingstocht door Rotterdam', 'A. Drive & Eat', 'B. Bicycle Diner', 'C. Bike & Bite', 'B'),
(84, 'MC', 'Entertainment', 'Wat is de bekendste escape room in Rotterdam', 'A. R’dam escape', 'B. Escape010', 'C. Room Escape', 'B'),
(85, 'MC', 'Entertainment', 'Welke bar in Rotterdam werd in 2009 de beste bar ter wereld benoemd', 'A. De Witte Aap', 'B. Het NRC', 'C. Café de beurs', 'A'),
(86, 'MC', 'Entertainment', 'Op welk Plein vindt jaarlijks het najaar kermis Rotterdam plaats', 'A. Mullepier', 'B. Pier 80', 'C. Schouwburgplein', 'A'),
(87, 'MC', 'Entertainment', 'Welke landen kun je behalve Nederland ook in miniwereld Rotterdam zien', 'A. Luxemburg en België', 'B. Duitsland en België', 'C. Duitsland en Frankrijk', 'A'),
(103,'MC', 'Sport', 'Welke olympiër groeide op in Rotterdam', 'A. Dorian van Rijsselberghe', 'B. Marhinde Verkerk', 'C. Edith Bosch', 'B'),
(104,'MC', 'Sport', 'Wat is een hockeyclub uit Rotterdam', 'A. HVG', 'B. Focus', 'C. HC Rotterdam', 'A'),
(106,'MC', 'Sport', 'In welk jaar is de honkbalclub Neptunes opgericht', 'A. 1850', 'B. 1875', 'C. 1900', 'C'),
(107,'MC', 'Sport', 'Op welke positie speelde Coen Moulijn voor Feyenoord en het Nederlands elftal', 'A. Rechtsbuiten', 'B. Linksback', 'C. Linksbuiten', 'C'),
(108,'MC', 'Sport', 'Hoeveel spelers staan per team op het veld bij lacrosse', 'A. 9', 'B. 10', 'C. 11', 'C'),
(109,'MC', 'Sport', 'Een honkbal is groter dan een softbal', 'A. Waar', 'B. Niet waar', NULL, 'B'),
(110,'MC', 'Sport', 'Welke manier van sport word het meest beoefend in Rotterdam', 'A. Fitness', 'B. Voetbal', 'C. Basketbal', 'A'),
(111,'MC', 'Sport', 'Hoeveel mensen staan er achter er slagman bij honkbal', 'A. 1', 'B. 2',  'C. 3', 'B' ),
(115,'MC', 'Sport', 'Een speler is buiten spel als', 'A. Hij zich veder van het doel bevindt als de keeper', 'B. Zich dichter bij de doellijn van de tegenstander bevindt dan de bal en de voorlaatste tegenstander', 'C. Zich buiten de lijn van het veld bevindt en de bal in het spel is', 'B');

CREATE TABLE QnA(
	Question_id 		int Primary key,
    Question_type 		Varchar(25),
	Question_Catagory	Varchar(30),
    Question 			varchar(250),
    Answer1				varchar(200),
    Answer2				varchar(200),
    Answer3				varchar(200),
    Correct_answer		varchar(200)
);

CREATE TABLE Score(
    Name varchar(30) Primary KEY,
    Score int,
	Wins int,
	losses int,
	);
    
	
	
use std::io;

pub fn next() -> String {
    let mut string = String::new();

    io::stdin().read_line(&mut string)
        .expect("Failed to read line");

	return string;
}

pub fn next_int() -> i64 {
	let mut number = String::new();

	io::stdin().read_line(&mut number)
		.expect("Failed to read line");

	let number: i64 = number.trim().parse()
        .expect("Please type a number!");

	return number;
}

pub fn next_long() -> f32 {
	let mut number = String::new();

	io::stdin().read_line(&mut number)
		.expect("Failed to read line");

	let number: f32 = number.trim().parse()
        .expect("Please type a number!");

	return number;
}

pub fn next_char() -> char {
	let mut character = String::new();

	io::stdin().read_line(&mut character)
		.expect("Failed to read line");

	let character: char = character.trim().parse()
        .expect("Please type a number!");

	return character;
}

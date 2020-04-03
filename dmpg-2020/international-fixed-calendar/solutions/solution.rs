use std::io;

fn main () {
	let mut buffer: String = String::new();
	io::stdin().read_line(&mut buffer)
				.expect("Failed to read from stdin.");
	
	let days = buffer.trim().to_string()
						.parse::<i32>().unwrap();
						
	if days == 365 {
		println!("Happy New Year!");
	} else {
		let day = if days == 28 { 28 } else { days % 28 };
		let month = days / 28; // ceil this somehow
		println!("{} {}", month, day);
	}
}

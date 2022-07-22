use std::fs::read_to_string;


fn pop_n_bits(n: u8, bits: &mut Vec<u8>) -> u64 {
    let mut result = 0;
    for _ in 0..n {
        result = (result << 1) | bits.pop().unwrap() as u64;
    }
    result
}


fn parse_next_packet(bits: &mut Vec<u8>) -> u64 {
    let mut version = pop_n_bits(3, bits);
    let ptype = pop_n_bits(3, bits);
    match ptype {
        4 => {
            let mut cont = true;
            while cont {
                cont = bits.pop().unwrap() != 0;
                pop_n_bits(4, bits);
            }
        },
        _ => {
            let length_id = bits.pop().unwrap();
            if length_id == 0 {
                let length_val = pop_n_bits(15, bits);
                let target_len = bits.len() - length_val as usize;
                while bits.len() > target_len {
                    let vver = parse_next_packet(bits);
                    version += vver;
                }
            } else {
                let num_subpackets = pop_n_bits(11, bits);
                for _ in 0..num_subpackets {
                    let vver = parse_next_packet(bits);
                    version += vver;
                }
            }
        },
    }
    version
}


fn main() {
    let content = read_to_string("input").unwrap();

    let mut bits: Vec<u8> = vec![];
    for c in content.trim().chars() {
        let hexdigit = c.to_digit(16).unwrap() as u8;
        bits.insert(0, (hexdigit & 0x8) >> 3);
        bits.insert(0, (hexdigit & 0x4) >> 2);
        bits.insert(0, (hexdigit & 0x2) >> 1);
        bits.insert(0, hexdigit & 0x1);
    }

    let mut result = 0;
    while bits.len() > 2 && bits.iter().any(|&d| d != 0) {
        result += parse_next_packet(&mut bits);
    }
    println!("result = {result:?}");
}

use std::fs::read_to_string;


fn pop_n_bits(n: u8, bits: &mut Vec<u8>) -> u64 {
    let mut result = 0;
    for _ in 0..n {
        result = (result << 1) | bits.pop().unwrap() as u64;
    }
    result
}


fn parse_next_packet(bits: &mut Vec<u8>) -> u64 {
    let _version = pop_n_bits(3, bits);
    let ptype = pop_n_bits(3, bits);
    let mut val = 0;
    match ptype {
        4 => {
            let mut cont = true;
            while cont {
                cont = bits.pop().unwrap() != 0;
                for _ in 0..4 {
                    val = (val << 1) | bits.pop().unwrap() as u64;
                }
            }
        },
        _ => {
            let length_id = bits.pop().unwrap();
            let mut acc = vec![];
            if length_id == 0 {
                let length_val = pop_n_bits(15, bits);
                let target_len = bits.len() - length_val as usize;
                while bits.len() > target_len {
                    acc.push(parse_next_packet(bits));
                }
            } else {
                let num_subpackets = pop_n_bits(11, bits);
                for _ in 0..num_subpackets {
                    acc.push(parse_next_packet(bits));
                }
            }
            match ptype {
                0 => val = acc.iter().sum(),
                1 => val = acc.iter().product(),
                2 => val = *acc.iter().min().unwrap(),
                3 => val = *acc.iter().max().unwrap(),
                5 => val = (acc[0] > acc[1]) as u64,
                6 => val = (acc[0] < acc[1]) as u64,
                7 => val = (acc[0] == acc[1]) as u64,
                _ => panic!("unknown ptype = {:?}", ptype),
            }
        },
    }
    val
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

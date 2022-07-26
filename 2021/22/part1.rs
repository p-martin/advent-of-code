use std::io::{BufReader, BufRead};
use std::fs::File;
use std::collections::HashSet;


fn main() {
    let mut xvals = vec![];
    let mut yvals = vec![];
    let mut zvals = vec![];
    let mut oncubes = HashSet::new();

    for (i, line) in BufReader::new(File::open("input").unwrap()).lines().flatten().enumerate() {
        if let [onoff, coords] = line.split_whitespace().collect::<Vec<_>>()[..] {
            for (j, coord) in coords.split(',').enumerate() {
                let mut limits = coord.split('=').skip(1).next().unwrap().split("..");
                let start = limits.next().unwrap().parse::<i64>().unwrap().max(-50);
                let end = limits.next().unwrap().parse::<i64>().unwrap().min(50);
                if start <= end {
                    match j {
                        0 => {
                            xvals.push((start, i as i64, true));
                            xvals.push((end + 1, i as i64, false));
                        },
                        1 => {
                            yvals.push((start, i as i64, true));
                            yvals.push((end + 1, i as i64, false));
                        },
                        2 => {
                            zvals.push((start, i as i64, true));
                            zvals.push((end + 1, i as i64, false));
                        },
                        _ => panic!("too many coords"),
                    }
                }
            }
            if onoff == "on" {
                oncubes.insert(i as i64);
            }
        }
    }

    let mut num_x = 0;
    let mut handled_until_x = 0;
    let mut relevant_ids_x = HashSet::new();
    xvals.sort();
    for &(x, id_x, add_x) in xvals.iter() {
        let mut num_y = 0;
        let mut handled_until_y = 0;
        let mut relevant_ids_y = HashSet::new();
        let mut part_yvals: Vec<_> = yvals.iter()
            .filter(|&p| relevant_ids_x.contains(&p.1))
            .collect();
        part_yvals.sort();
        for &(y, id_y, add_y) in part_yvals.iter() {
            let mut num_z = 0;
            let mut handled_until_z = 0;
            let mut relevant_ids_z = HashSet::<i64>::new();
            let mut part_zvals: Vec<_> = zvals.iter()
                .filter(|&p| relevant_ids_y.contains(&p.1))
                .collect();
            part_zvals.sort();
            for &(z, id_z, add_z) in part_zvals.iter() {
                if relevant_ids_z.len() > 0 &&
                        oncubes.contains(relevant_ids_z.iter().max().unwrap()) {
                    num_z += z - handled_until_z;
                }
                if *add_z {
                    relevant_ids_z.insert(*id_z);
                } else {
                    relevant_ids_z.remove(id_z);
                }
                handled_until_z = *z;
            }
            num_y += (y - handled_until_y) * num_z;
            if *add_y {
                relevant_ids_y.insert(*id_y);
            } else {
                relevant_ids_y.remove(id_y);
            }
            handled_until_y = *y;
        }
        num_x += (x - handled_until_x) * num_y;
        if add_x {
            relevant_ids_x.insert(id_x);
        } else {
            relevant_ids_x.remove(&id_x);
        }
        handled_until_x = x;
    }

    println!("result = {:?}", num_x);
}

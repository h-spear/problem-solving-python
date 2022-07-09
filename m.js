const fs = require('fs');

const home_dir = './';

const programmers_dir = './programmers';
const leetcode_dir = './leetcode';
const fail_dir = './fail';
const note_dir = './my_note';

const result = { home: [], programmers: [], leetcode: [] };

const output_file = 'readme.md';
const baekjoon_id = 'ki9014';
const baekjoon_rank_svg = 'https://static.solved.ac/tier_small/18.svg';

function check_condition(p) {
    if (
        './' + p.name === programmers_dir ||
        './' + p.name === leetcode_dir ||
        './' + p.name === fail_dir ||
        './' + p.name === note_dir
    ) {
        return false;
    }
    if (!p.isDirectory()) {
        return false;
    }
    if (p.name[0] == '.') {
        return false;
    }
    return true;
}

fs.readdirSync(home_dir, { withFileTypes: true }).forEach((p) => {
    const name = p.name;
    const path = './' + name;
    if (!check_condition(p)) {
        return;
    }
    result['home'].push({ name, length: fs.readdirSync(path).length });
});

// programmers
fs.readdirSync(programmers_dir, { withFileTypes: true }).forEach((p) => {
    const name = p.name;
    const path = programmers_dir + '/' + name;

    if (!check_condition(p)) {
        return;
    }
    result['programmers'].push({
        name,
        length: fs.readdirSync(path).length,
    });
});

// leetcode
fs.readdirSync(leetcode_dir, { withFileTypes: true }).forEach((p) => {
    const name = p.name;
    const path = leetcode_dir + '/' + name;

    if (!p.isDirectory()) {
        return;
    }
    if (name[0] == '.') {
        return;
    }

    result['leetcode'].push({
        name,
        length: fs.readdirSync(path).length,
    });
});

// write md file
if (!fs.existsSync(output_file)) {
    fs.openSync(output_file, 'w', 666);
}

fs.writeFileSync(output_file, '');

// Baekjoon
let baekjoon_sum = 0;
fs.appendFileSync(
    output_file,
    `## BAEKJOON [<img src=${baekjoon_rank_svg} width="15"/>](https://www.acmicpc.net/user/${baekjoon_id}) \n|    Algorithm    | solved |\n| :-------------: | :----: |\n`,
    'utf-8'
);
result['home'].forEach((v) => {
    const { name, length } = v;
    temp = '|' + name + '|' + length + '|\n';
    baekjoon_sum += length;
    fs.appendFileSync(output_file, temp, 'utf-8');
});
fs.appendFileSync(
    output_file,
    '| **sum** | **' + baekjoon_sum + '**|\n&nbsp;\n',
    'utf-8'
);
console.log('baekjoon solved ' + baekjoon_sum + '!');

// 프로그래머스
let programmers_sum = 0;
fs.appendFileSync(
    output_file,
    '## Programmers\n|    Level    | solved |\n| :-------------: | :----: |\n',
    'utf-8'
);
result['programmers'].forEach((v) => {
    const { name, length } = v;
    temp = '|' + name + '|' + length + '|\n';
    programmers_sum += length;
    fs.appendFileSync(output_file, temp, 'utf-8');
});
fs.appendFileSync(
    output_file,
    '| **sum** | **' + programmers_sum + '**|\n&nbsp;\n',
    'utf-8'
);
console.log('programmers solved ' + programmers_sum + '!');

// 리트코드
let leetcode_sum = 0;
fs.appendFileSync(
    output_file,
    '## LeetCode\n|    Algorithm    | solved |\n| :-------------: | :----: |\n',
    'utf-8'
);
result['leetcode'].forEach((v) => {
    const { name, length } = v;
    temp = '|' + name + '|' + length + '|\n';
    leetcode_sum += length;
    fs.appendFileSync(output_file, temp, 'utf-8');
});
fs.appendFileSync(
    output_file,
    '| **sum** | **' + leetcode_sum + '**|\n',
    'utf-8'
);
console.log('leetcode solved ' + leetcode_sum + '!\n');
console.log('saved successfully! ' + output_file);

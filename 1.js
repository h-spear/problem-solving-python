const fs = require('fs');
const { runBaekjoonReadmeGenerator } = require('./baekjoon/boj.js');

const home_dir = './';

const baekjoon_dir = './baekjoon';
const programmers_dir = './programmers';
const leetcode_dir = './leetcode';
const swacademy_dir = './sw_expert_academy';
const note_dir = './my_note';

const result = {
    baekjoon: [],
    programmers: [],
    leetcode: [],
    swacademy: [],
};

const output_file = 'readme.md';

function check_condition(p) {
    if (
        './' + p.name === baekjoon_dir ||
        './' + p.name === programmers_dir ||
        './' + p.name === leetcode_dir ||
        './' + p.name === swacademy_dir ||
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

fs.readdirSync(baekjoon_dir, { withFileTypes: true }).forEach((p) => {
    const name = p.name;
    const path = baekjoon_dir + '/' + name;
    if (!check_condition(p)) {
        return;
    }
    result['baekjoon'].push({ name, length: fs.readdirSync(path).length });
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

// sw academy
fs.readdirSync(swacademy_dir, { withFileTypes: true }).forEach((p) => {
    const name = p.name;
    const path = swacademy_dir + '/' + name;

    if (!check_condition(p)) {
        return;
    }
    result['swacademy'].push({
        name,
        length: fs.readdirSync(path).length,
    });
});

// leetcode;
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

runBaekjoonReadmeGenerator();

// write md file
if (!fs.existsSync(output_file)) {
    fs.openSync(output_file, 'w', 666);
}

fs.writeFileSync(output_file, '');

// Baekjoon
let baekjoon_sum = 0;
fs.appendFileSync(
    output_file,
    `## BAEKJOON \n|    Algorithm    | solved |\n| :-------------: | :----: |\n`,
    'utf-8'
);
result['baekjoon'].forEach((v) => {
    const { name, length } = v;
    temp = '|' + name + '|' + length + '|\n';
    baekjoon_sum += length;
    fs.appendFileSync(output_file, temp, 'utf-8');
});
fs.appendFileSync(
    output_file,
    '| **sum** | **' + baekjoon_sum + '**|\n\n',
    'utf-8'
);
console.log('baekjoon solved ' + baekjoon_sum + '!');

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
console.log('leetcode solved ' + leetcode_sum + '!');

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
    '| **sum** | **' + programmers_sum + '**|\n\n',
    'utf-8'
);
console.log('programmers solved ' + programmers_sum + '!');

// sw academy
let swacademy_sum = 0;
fs.appendFileSync(
    output_file,
    '## SW Expert Academy\n|    Difficulty    | solved |\n| :-------------: | :----: |\n',
    'utf-8'
);
result['swacademy'].forEach((v) => {
    const { name, length } = v;
    temp = '|' + name + '|' + length + '|\n';
    swacademy_sum += length;
    fs.appendFileSync(output_file, temp, 'utf-8');
});
fs.appendFileSync(
    output_file,
    '| **sum** | **' + swacademy_sum + '**|\n\n',
    'utf-8'
);
console.log('sw academy solved ' + swacademy_sum + '!');
console.log('saved successfully! ' + output_file);

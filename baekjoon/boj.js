const fs = require('fs');

const except_list = ['out', '.idea', 'fail'];
const output_file = './baekjoon/readme.md';
const algMap = {
    back_tracking: 'Back Tracking',
    binary_search: 'Binary Search',
    bitmask: 'Bitmask',
    brute_force: 'Bruteforce',
    data_structure: 'Data Structure',
    'dfs&bfs': 'DFS & BFS',
    divide_and_conquer: 'Divide and Conquer',
    dynamic_programming: 'Dynamic Programming',
    geometry: 'Geometry',
    graph: 'Graph',
    greedy: 'Greedy',
    implementation: 'Implementation',
    math: 'Math',
    network_flow: 'Network Flow',
    prefix_sum: 'Prefix Sum',
    samsung: 'Samsung',
    segment_tree: 'Segment Tree',
    shortest_path: 'Shortest Path',
    sorting: 'Sorting',
    string: 'String',
    tree: 'Tree',
    two_pointer: 'Two Pointer',
    'union-find': 'Union Find',
};
const bojLevelUrlPrefix = 'https://static.solved.ac/tier_small/';
const bojLevelUrlSuffix = '.svg';
const bojProblemBaseUrl = 'https://solved.ac/api/v3/problem/lookup?problemIds=';

const problemMap = {};
const problemInfos = {};

function checkCondition(p) {
    if (!p.isDirectory()) {
        return false;
    }
    if (p.name[0] == '.') {
        return false;
    }
    if (except_list.indexOf(p.name) != -1) {
        return false;
    }
    return true;
}

async function getProblemInfos(problemNumbers) {
    const response = await fetch(bojProblemBaseUrl + problemNumbers.join(','))
        .then((response) => response.json())
        .then((data) => {
            for (const prob of data) {
                problemInfos[prob['problemId']]['title'] = prob['titleKo'];
                problemInfos[prob['problemId']]['level'] = prob['level'];
            }
        });
    return response;
}

async function main() {
    fs.readdirSync('./baekjoon', { withFileTypes: true }).forEach((p) => {
        const alg = p.name;
        const path = './baekjoon/' + alg;
        if (!checkCondition(p)) {
            return;
        }
        problemMap[alg] = [];
        fs.readdirSync(path).forEach((file) => {
            const problemNumber = fs
                .readFileSync(path + '/' + file, 'utf-8')
                .replace('\r', '')
                .split('\n')[0]
                .split('/')
                .pop();
            problemInfos[problemNumber] = {
                title: '',
                level: 0,
                file: file,
                path: './' + alg + '/' + file,
            };
            if (problemNumber.length > 5) console.log(path, file);
            problemMap[alg].push(problemNumber);
            // const data = fs
            //     .readFileSync(path + '/' + file, 'utf-8')
            //     .split('\n')[0]
            //     .split('/')
            //     .pop();
            // console.log(file, data);
        });
        problemMap[alg].sort((a, b) => (parseInt(a) < parseInt(b) ? -1 : 1));
    });

    const problemNumbers = [];
    for (const problem in problemInfos) {
        problemNumbers.push(problem);
    }
    for (let i = 0, end = problemNumbers.length; i < end; i += 30) {
        await getProblemInfos(problemNumbers.slice(i, i + 30));
    }

    // write md file
    if (!fs.existsSync(output_file)) {
        fs.openSync(output_file, 'w', 666);
    }
    fs.writeFileSync(output_file, '');

    // // 백준
    fs.appendFileSync(output_file, '## Baekjoon', 'utf-8');

    for (const alg in problemMap) {
        fs.appendFileSync(
            output_file,
            `\n---\n\n### ${algMap[alg]}\n|    Tier    | No | Problem | Code | \n| :-------------: | :----: | :----: | :----: |\n`,
            'utf-8'
        );
        for (const problemNumber of problemMap[alg]) {
            fs.appendFileSync(
                output_file,
                `|    <img src="${
                    bojLevelUrlPrefix +
                    problemInfos[problemNumber]['level'] +
                    bojLevelUrlSuffix
                }" width="20"></img>    | <a href="http://boj.kr/${problemNumber}">${problemNumber}</a> | ${
                    problemInfos[problemNumber]['title']
                } | <a href="${problemInfos[problemNumber]['path']}">${
                    problemInfos[problemNumber]['file']
                }</a> |\n`,
                'utf-8'
            );
        }
    }
    console.log('saved baekjoon problem infos!');
}

module.exports.runBaekjoonReadmeGenerator = main;

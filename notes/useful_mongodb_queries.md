# Useful MongoDB Queries with Explanation

## 1\. OR Query

Find documents where either `name` OR `email` matches the search value.

```
const query = {
  $or: [
    { name: { $regex: search, $options: "i" } },
    { email: { $regex: search, $options: "i" } },
  ],
};
```

---

## 2\. AND Query

Find documents where ALL conditions are true.

```
const query = {
  $and: [{ age: { $gte: 18 } }, { status: "active" }],
};
```

---

## 3\. Search Multiple Fields

Search across multiple fields using regex.

```
const query = {
  $or: [
    { name: { $regex: search, $options: "i" } },
    { email: { $regex: search, $options: "i" } },
    { city: { $regex: search, $options: "i" } },
  ],
};
```

---

## 4\. Exact Match

Find documents with an exact value.

```
const query = {
  email: "test@gmail.com",
};
```

---

## 5\. NOT Equal

Find documents where field value is NOT equal.

```
const query = {
  status: { $ne: "deleted" },
};
```

---

## 6\. IN Operator

Find documents where value exists in an array.

```
const query = {
  role: { $in: ["admin", "manager"] },
};
```

---

## 7\. NOT IN Operator

Exclude values from query results.

```
const query = {
  role: { $nin: ["banned", "blocked"] },
};
```

---

## 8\. Greater Than / Less Than

Numeric comparisons.

```
const query = {
  age: { $gt: 18 },
};
```

```
const query = {
  age: { $lt: 60 },
};
```

```
const query = {
  age: {
    $gte: 18,
    $lte: 60,
  },
};
```

---

## 9\. Field Exists

Find documents where field exists.

```
const query = {
  phone: { $exists: true },
};
```

---

## 10\. Field Does NOT Exist

Find documents without a field.

```
const query = {
  phone: { $exists: false },
};
```

---

## 11\. Null Check

Find documents where field is null.

```
const query = {
  phone: null,
};
```

---

## 12\. Array Contains

Find array containing specific value.

```
const query = {
  skills: "Node.js",
};
```

---

## 13\. Array Contains Multiple Values

Match all array values.

```
const query = {
  skills: { $all: ["Node.js", "MongoDB"] },
};
```

---

## 14\. Array Size

Find arrays with specific length.

```
const query = {
  skills: { $size: 3 },
};
```

---

## 15\. Nested Object Query

Query nested fields using dot notation.

```
const query = {
  "address.city": "Delhi",
};
```

---

## 16\. Regex Starts With

Find values starting with text.

```
const query = {
  name: { $regex: "^john", $options: "i" },
};
```

---

## 17\. Regex Ends With

Find values ending with text.

```
const query = {
  email: { $regex: "gmail.com$", $options: "i" },
};
```

---

## 18\. Regex Contains

Find values containing text.

```
const query = {
  name: { $regex: "oh", $options: "i" },
};
```

---

## 19\. Date Range Query

Find documents within date range.

```
const query = {
  createdAt: {
    $gte: new Date("2025-01-01"),
    $lte: new Date("2025-12-31"),
  },
};
```

---

## 20\. Sort Query

Sort documents ascending or descending.

```
User.find(query).sort({ createdAt: -1 });
```

```
.sort({ age: 1 })
```

---

## 21\. Limit Query

Limit number of results.

```
User.find().limit(10);
```

---

## 22\. Pagination

Pagination using skip and limit.

```
const page = 2;
const limit = 10;

User.find()
  .skip((page - 1) * limit)
  .limit(limit);
```

---

## 23\. Select Specific Fields

Return selected fields only.

```
User.find({}, "name email");
```

Exclude fields:

```
User.find({}, { password: 0 });
```

---

## 24\. Count Documents

Count matching documents.

```
User.countDocuments(query);
```

---

## 25\. Distinct Values

Get unique field values.

```
User.distinct("city");
```

---

## 26\. Update One

Update single document.

```
User.updateOne({ _id: id }, { $set: { name: "John" } });
```

---

## 27\. Update Many

Update multiple documents.

```
User.updateMany({ status: "inactive" }, { $set: { status: "active" } });
```

---

## 28\. Increment Value

Increase numeric value.

```
User.updateOne({ _id: id }, { $inc: { loginCount: 1 } });
```

---

## 29\. Push Into Array

Add item to array.

```
User.updateOne({ _id: id }, { $push: { skills: "React" } });
```

---

## 30\. Pull From Array

Remove item from array.

```
User.updateOne({ _id: id }, { $pull: { skills: "PHP" } });
```

---

## 31\. Delete One

Delete single document.

```
User.deleteOne({ _id: id });
```

---

## 32\. Delete Many

Delete multiple documents.

```
User.deleteMany({ status: "deleted" });
```

---

## 33\. Find One

Find first matching document.

```
User.findOne({ email: "test@gmail.com" });
```

---

## 34\. Find By ID

Find document using ObjectId.

```
User.findById(id);
```

---

## 35\. Aggregate Match

Filter documents in aggregation.

```
User.aggregate([
  {
    $match: {
      status: "active",
    },
  },
]);
```

---

## 36\. Aggregate Group

Group documents and count.

```
User.aggregate([
  {
    $group: {
      _id: "$city",
      total: { $sum: 1 },
    },
  },
]);
```

---

## 37\. Aggregate Project

Select fields in aggregation.

```
User.aggregate([
  {
    $project: {
      name: 1,
      email: 1,
    },
  },
]);
```

---

## 38\. Lookup (JOIN)

Join collections.

```
Order.aggregate([
  {
    $lookup: {
      from: "users",
      localField: "userId",
      foreignField: "_id",
      as: "user",
    },
  },
]);
```

---

## 39\. Unwind Array

Convert array items into documents.

```
User.aggregate([
  {
    $unwind: "$skills",
  },
]);
```

---

## 40\. Text Search

Create text index:

```
db.users.createIndex({
  name: "text",
  email: "text",
});
```

Search text:

```
db.users.find({
  $text: {
    $search: "john",
  },
});
```

---

## 41\. Case-Insensitive Search

Case-insensitive exact search.

```
const query = {
  username: {
    $regex: "^john$",
    $options: "i",
  },
};
```

---

## 42\. Dynamic Search Query

Build query dynamically.

```
const query = {};

if (name) {
  query.name = { $regex: name, $options: "i" };
}

if (email) {
  query.email = { $regex: email, $options: "i" };
}

if (status) {
  query.status = status;
}
```

---

## 43\. Dynamic Filter + Pagination

Production-ready filtering.

```
const query = {};

if (search) {
  query.$or = [
    { name: { $regex: search, $options: "i" } },
    { email: { $regex: search, $options: "i" } },
  ];
}

const users = await User.find(query)
  .sort({ createdAt: -1 })
  .skip((page - 1) * limit)
  .limit(limit);
```

---

## 44\. Mongoose Populate

Populate referenced documents.

```
Post.find().populate("userId");
```

Specific fields:

```
.populate('userId', 'name email')
```

---

## 45\. Find Latest Record

Get newest document.

```
User.findOne().sort({ createdAt: -1 });
```

---

## 46\. Find Oldest Record

Get oldest document.

```
User.findOne().sort({ createdAt: 1 });
```

---

## 47\. Duplicate Detection

Find duplicate values.

```
User.aggregate([
  {
    $group: {
      _id: "$email",
      count: { $sum: 1 },
    },
  },
  {
    $match: {
      count: { $gt: 1 },
    },
  },
]);
```

---

## 48\. Conditional Query

Add conditions dynamically.

```
const query = {
  isDeleted: false,
  ...(role && { role }),
  ...(status && { status }),
};
```

---

## 49\. ObjectId Query

Convert string to ObjectId.

```
const mongoose = require("mongoose");

const query = {
  _id: new mongoose.Types.ObjectId(id),
};
```

---

## 50\. Combine OR + AND

Use both AND and OR.

```
const query = {
  $and: [
    { status: "active" },
    {
      $or: [
        { name: { $regex: search, $options: "i" } },
        { email: { $regex: search, $options: "i" } },
      ],
    },
  ],
};
```

---

# Bonus: Production Query Example

Complete real-world query example.

```
const query = {
  isDeleted: false,
};

if (search) {
  query.$or = [
    { name: { $regex: search, $options: "i" } },
    { email: { $regex: search, $options: "i" } },
    { phone: { $regex: search, $options: "i" } },
  ];
}

if (status) {
  query.status = status;
}

const data = await User.find(query)
  .sort({ createdAt: -1 })
  .skip((page - 1) * limit)
  .limit(limit);
```

# Real Interview-Level Practice Tasks

Try solving these yourself:

1.  Find users whose name starts with "A"
2.  Find users having both MongoDB and Node.js skills
3.  Increase salary by 10% for all active users
4.  Find top 2 highest-paid users
5.  Remove "Java" skill from all users
6.  Find duplicate cities
7.  Count users city-wise
8.  Find users not from Delhi
9.  Find users with exactly 2 skills
10.  Create an index on `email`

```
 [
  {
    name: "Aman",
    age: 22,
    city: "Delhi",
    skills: [
      "MongoDB",
      "Node.js"
    ],
    salary: 40000,
    active: true
  },
  {
    name: "Riya",
    age: 25,
    city: "Mumbai",
    skills: [
      "React",
      "MongoDB"
    ],
    salary: 60000,
    active: true
  },
  {
    name: "Karan",
    age: 28,
    city: "Pune",
    skills: [
      "Python",
      "Django"
    ],
    salary: 75000,
    active: false
  },
  {
    name: "Neha",
    age: 21,
    city: "Delhi",
    skills: [
      "Java",
      "Spring"
    ],
    salary: 50000,
    active: true
  }
]
```

### 1\. Find users whose name starts with "A"

```
db.users.find({
  name: { $regex: "^A", $options: "i" }
})
```

---

### 2\. Find users having both MongoDB and Node.js skills

```
db.users.find({
  skills: { $all: ["MongoDB", "Node.js"] }
})
```

---

### 3\. Increase salary by 10% for all active users

```
db.users.updateMany(
  { status: "active" },
  { $mul: { salary: 1.10 } }
)
```

---

### 4\. Find top 2 highest-paid users

```
db.users.find()
  .sort({ salary: -1 })
  .limit(2)
```

---

### 5\. Remove "Java" skill from all users

```
db.users.updateMany(
  {},
  { $pull: { skills: "Java" } }
)
```

---

### 6\. Find duplicate cities

```
db.users.aggregate([
  {
    $group: {
      _id: "$city",
      count: { $sum: 1 }
    }
  },
  {
    $match: {
      count: { $gt: 1 }
    }
  }
])
```

---

### 7\. Count users city-wise

```
db.users.aggregate([
  {
    $group: {
      _id: "$city",
      totalUsers: { $sum: 1 }
    }
  }
])
```

---

### 8\. Find users not from Delhi

```
db.users.find({
  city: { $ne: "Delhi" }
})
```

---

### 9\. Find users with exactly 2 skills

```
db.users.find({
  skills: { $size: 2 }
})
```

---

### 10\. Create an index on email

```
db.users.createIndex({
  email: 1
})
```

Unique index version:

```
db.users.createIndex(
  { email: 1 },
  { unique: true }
)
```

# 50 MongoDB Practice Questions — Answers

Using MongoDB collection: `db.users`

---

# Beginner Level (1–15)

### 1\. Find all users

```
db.users.find()
```

### 2\. Find users whose age is greater than 25

```
db.users.find({ age: { $gt: 25 } })
```

### 3\. Find users from Delhi

```
db.users.find({ city: "Delhi" })
```

### 4\. Find active users

```
db.users.find({ active: true })
```

### 5\. Find users whose salary is less than 50,000

```
db.users.find({ salary: { $lt: 50000 } })
```

### 6\. Show only name and city

```
db.users.find({}, { name: 1, city: 1 })
```

### 7\. Exclude \_id from results

```
db.users.find({}, { _id: 0 })
```

### 8\. Find users whose age is exactly 22

```
db.users.find({ age: 22 })
```

### 9\. Find users who are not active

```
db.users.find({ active: false })
```

### 10\. Find users with salary greater than or equal to 60,000

```
db.users.find({ salary: { $gte: 60000 } })
```

### 11\. Find users living in Mumbai or Pune

```
db.users.find({
  city: { $in: ["Mumbai", "Pune"] }
})
```

### 12\. Find users whose city is not Delhi

```
db.users.find({
  city: { $ne: "Delhi" }
})
```

### 13\. Find users whose age is between 20 and 30

```
db.users.find({
  age: { $gte: 20, $lte: 30 }
})
```

### 14\. Find users with the skill "MongoDB"

```
db.users.find({
  skills: "MongoDB"
})
```

### 15\. Count total users

```
db.users.countDocuments()
```

---

# Intermediate Level (16–35)

## Operators & Arrays

### 16\. Find users with both "MongoDB" and "Node.js" skills

```
db.users.find({
  skills: { $all: ["MongoDB", "Node.js"] }
})
```

### 17\. Find users having either "React" or "Angular" skill

```
db.users.find({
  skills: { $in: ["React", "Angular"] }
})
```

### 18\. Find users whose name starts with "A"

```
db.users.find({
  name: { $regex: "^A", $options: "i" }
})
```

### 19\. Find users whose name ends with "a"

```
db.users.find({
  name: { $regex: "a$", $options: "i" }
})
```

### 20\. Find users whose name contains "an"

```
db.users.find({
  name: { $regex: "an", $options: "i" }
})
```

### 21\. Find users whose age is not 25

```
db.users.find({
  age: { $ne: 25 }
})
```

### 22\. Find users whose salary is in \[40000, 50000, 60000\]

```
db.users.find({
  salary: { $in: [40000, 50000, 60000] }
})
```

### 23\. Find users with exactly 2 skills

```
db.users.find({
  skills: { $size: 2 }
})
```

### 24\. Find users with more than 2 skills

```
db.users.find({
  "skills.2": { $exists: true }
})
```

### 25\. Sort users by age ascending

```
db.users.find().sort({ age: 1 })
```

### 26\. Sort users by salary descending

```
db.users.find().sort({ salary: -1 })
```

### 27\. Skip first 2 users

```
db.users.find().skip(2)
```

### 28\. Limit result to 3 users

```
db.users.find().limit(3)
```

### 29\. Find top 3 highest-paid users

```
db.users.find()
  .sort({ salary: -1 })
  .limit(3)
```

### 30\. Find youngest user

```
db.users.find()
  .sort({ age: 1 })
  .limit(1)
```

### 31\. Find users where city exists

```
db.users.find({
  city: { $exists: true }
})
```

### 32\. Find users where phone number does not exist

```
db.users.find({
  phone: { $exists: false }
})
```

### 33\. Find users with null values in email

```
db.users.find({
  email: null
})
```

### 34\. Find users whose skills array contains "Python"

```
db.users.find({
  skills: "Python"
})
```

### 35\. Count active users from Delhi

```
db.users.countDocuments({
  active: true,
  city: "Delhi"
})
```

---

# Update Practice (36–42)

## Update Queries

### 36\. Increase salary of all active users by 5000

```
db.users.updateMany(
  { active: true },
  { $inc: { salary: 5000 } }
)
```

### 37\. Change city from Delhi to New Delhi

```
db.users.updateMany(
  { city: "Delhi" },
  { $set: { city: "New Delhi" } }
)
```

### 38\. Add "Express.js" skill to Aman

```
db.users.updateOne(
  { name: "Aman" },
  { $push: { skills: "Express.js" } }
)
```

### 39\. Remove "Java" skill from all users

```
db.users.updateMany(
  {},
  { $pull: { skills: "Java" } }
)
```

### 40\. Rename field salary to income

```
db.users.updateMany(
  {},
  { $rename: { salary: "income" } }
)
```

### 41\. Set active to false for users older than 30

```
db.users.updateMany(
  { age: { $gt: 30 } },
  { $set: { active: false } }
)
```

### 42\. Add a new field experience: 2 to all users

```
db.users.updateMany(
  {},
  { $set: { experience: 2 } }
)
```

---

# Delete Practice (43–45)

## Delete Queries

### 43\. Delete users who are inactive

```
db.users.deleteMany({
  active: false
})
```

### 44\. Delete users whose age is less than 18

```
db.users.deleteMany({
  age: { $lt: 18 }
})
```

### 45\. Delete users from Pune

```
db.users.deleteMany({
  city: "Pune"
})
```

---

# Aggregation Practice (46–50)

## Aggregation Pipeline

### 46\. Find average salary of all users

```
db.users.aggregate([
  {
    $group: {
      _id: null,
      averageSalary: { $avg: "$salary" }
    }
  }
])
```

### 47\. Find maximum salary

```
db.users.aggregate([
  {
    $group: {
      _id: null,
      maxSalary: { $max: "$salary" }
    }
  }
])
```

### 48\. Group users by city and count them

```
db.users.aggregate([
  {
    $group: {
      _id: "$city",
      totalUsers: { $sum: 1 }
    }
  }
])
```

### 49\. Find total salary city-wise

```
db.users.aggregate([
  {
    $group: {
      _id: "$city",
      totalSalary: { $sum: "$salary" }
    }
  }
])
```

### 50\. Find cities having more than 2 users

```
db.users.aggregate([
  {
    $group: {
      _id: "$city",
      totalUsers: { $sum: 1 }
    }
  },
  {
    $match: {
      totalUsers: { $gt: 2 }
    }
  }
])
```

---

# Bonus Advanced Challenges

### Pagination

```
db.users.find()
  .skip(10)
  .limit(5)
```

### Create Index

```
db.users.createIndex({ email: 1 })
```

### $lookup (JOIN)

```
db.orders.aggregate([
  {
    $lookup: {
      from: "users",
      localField: "userId",
      foreignField: "_id",
      as: "userDetails"
    }
  }
])
```

### $unwind

```
db.users.aggregate([
  { $unwind: "$skills" }
])
```

### $project

```
db.users.aggregate([
  {
    $project: {
      name: 1,
      city: 1
    }
  }
])
```

### Leaderboard

```
db.users.find()
  .sort({ salary: -1 })
  .limit(10)
```

### Nested Document Query

```
db.users.find({
  "address.city": "Delhi"
})
```

### Text Search

```
db.users.createIndex({ bio: "text" })

db.users.find({
  $text: { $search: "developer" }
})
```

### Transactions

```
session.startTransaction()
```

### Role-Based Query

```
db.users.find({
  role: "admin"
})
```

# Most Important Aggregation Stages

| Stage | Purpose |
| --- | --- |
| `$match` | Filter documents |
| `$group` | Group documents |
| `$project` | Select/modify fields |
| `$sort` | Sort data |
| `$limit` | Limit results |
| `$skip` | Skip documents |
| `$unwind` | Break array into documents |
| `$lookup` | Join collections |
| `$addFields` | Add new fields |
| `$count` | Count documents |

---

# 1\. `$match`

Works like `find()`.

## Active users

```
db.users.aggregate([
  {
    $match: { active: true }
  }
])
```

---

# 2\. `$group`

Groups documents.

## Count users city-wise

```
db.users.aggregate([
  {
    $group: {
      _id: "$city",
      totalUsers: { $sum: 1 }
    }
  }
])
```

---

# 3\. `$avg`

Average calculation.

## Average salary

```
db.users.aggregate([
  {
    $group: {
      _id: null,
      avgSalary: { $avg: "$salary" }
    }
  }
])
```

---

# 4\. `$max` and `$min`

## Highest salary

```
db.users.aggregate([
  {
    $group: {
      _id: null,
      highestSalary: { $max: "$salary" }
    }
  }
])
```

---

## Lowest salary

```
db.users.aggregate([
  {
    $group: {
      _id: null,
      lowestSalary: { $min: "$salary" }
    }
  }
])
```

---

# 5\. `$sum`

## Total salary

```
db.users.aggregate([
  {
    $group: {
      _id: null,
      totalSalary: { $sum: "$salary" }
    }
  }
])
```

---

# 6\. `$project`

Choose fields or create computed fields.

## Show name and yearly salary

```
db.users.aggregate([
  {
    $project: {
      name: 1,
      yearlySalary: { $multiply: ["$salary", 12] }
    }
  }
])
```

---

# 7\. `$sort`

## Sort by salary descending

```
db.users.aggregate([
  {
    $sort: { salary: -1 }
  }
])
```

---

# 8\. `$limit`

## Top 2 highest salary users

```
db.users.aggregate([
  { $sort: { salary: -1 } },
  { $limit: 2 }
])
```

---

# 9\. `$skip`

## Skip first 2 users

```
db.users.aggregate([
  { $skip: 2 }
])
```

---

# 10\. `$unwind`

Converts array items into separate documents.

## Separate all skills

```
db.users.aggregate([
  {
    $unwind: "$skills"
  }
])
```

### Before

```
skills: ["MongoDB", "Node.js"]
```

### After

```
skills: "MongoDB"
skills: "Node.js"
```

---

# 11\. `$lookup` (JOIN)

Suppose:

## orders collection

```
{
  userId: 1,
  product: "Laptop"
}
```

## Join users with orders

```
db.users.aggregate([
  {
    $lookup: {
      from: "orders",
      localField: "_id",
      foreignField: "userId",
      as: "orders"
    }
  }
])
```

---

# 12\. `$count`

## Count active users

```
db.users.aggregate([
  { $match: { active: true } },
  { $count: "totalActiveUsers" }
])
```

---

# 13\. `$addFields`

Adds new field dynamically.

## Add bonus field

```
db.users.aggregate([
  {
    $addFields: {
      bonus: 5000
    }
  }
])
```

---

# 14\. Multiple Conditions

## Active users from Delhi

```
db.users.aggregate([
  {
    $match: {
      active: true,
      city: "Delhi"
    }
  }
])
```

---

# 15\. Group + Sum

## Total salary city-wise

```
db.users.aggregate([
  {
    $group: {
      _id: "$city",
      totalSalary: { $sum: "$salary" }
    }
  }
])
```

---

# 16\. Group + Average

## Average salary city-wise

```
db.users.aggregate([
  {
    $group: {
      _id: "$city",
      avgSalary: { $avg: "$salary" }
    }
  }
])
```

---

# 17\. `$push`

Push values into array while grouping.

## Collect names city-wise

```
db.users.aggregate([
  {
    $group: {
      _id: "$city",
      users: { $push: "$name" }
    }
  }
])
```

---

# 18\. `$first` and `$last`

## First user from each city

```
db.users.aggregate([
  {
    $group: {
      _id: "$city",
      firstUser: { $first: "$name" }
    }
  }
])
```

---

# 19\. Pagination

## Page 2 with 5 records

```
db.users.aggregate([
  { $skip: 5 },
  { $limit: 5 }
])
```

---

# 20\. Complex Pipeline Example

## Top active users by salary

```
db.users.aggregate([
  {
    $match: { active: true }
  },
  {
    $sort: { salary: -1 }
  },
  {
    $project: {
      name: 1,
      city: 1,
      salary: 1
    }
  },
  {
    $limit: 3
  }
])
```

---

# Most Important Aggregation Operators

| Operator | Meaning |
| --- | --- |
| `$sum` | Total |
| `$avg` | Average |
| `$max` | Highest value |
| `$min` | Lowest value |
| `$push` | Create array |
| `$addToSet` | Unique array values |
| `$multiply` | Multiply |
| `$divide` | Divide |
| `$subtract` | Subtract |
| `$cond` | If-else |

---

# Frequently Asked Interview Questions

## Find duplicate cities

```
db.users.aggregate([
  {
    $group: {
      _id: "$city",
      count: { $sum: 1 }
    }
  },
  {
    $match: {
      count: { $gt: 1 }
    }
  }
])
```

---

## Find second highest salary

```
db.users.aggregate([
  { $sort: { salary: -1 } },
  { $skip: 1 },
  { $limit: 1 }
])
```

---

## Count skills frequency

```
db.users.aggregate([
  { $unwind: "$skills" },
  {
    $group: {
      _id: "$skills",
      total: { $sum: 1 }
    }
  }
])
```

---

# Aggregation Pipeline Order (Very Important)

Usually best order:

```
[
  { $match },
  { $project },
  { $group },
  { $sort },
  { $skip },
  { $limit }
]
```

Filter early for better performance.

# MongoDB Aggregation — In Depth Guide

Aggregation in MongoDB is used to:

*   filter data
*   transform data
*   group data
*   calculate statistics
*   join collections
*   reshape documents
*   build analytics/reporting pipelines

Think of aggregation like a **data processing pipeline**.

---

# 1\. What is Aggregation?

Suppose you have this collection:

```
db.users.find()

[
  {
    name: "Aman",
    city: "Delhi",
    salary: 40000
  },
  {
    name: "Riya",
    city: "Mumbai",
    salary: 60000
  },
  {
    name: "Karan",
    city: "Delhi",
    salary: 80000
  }
]
```

Now you want:

*   average salary
*   total salary city-wise
*   highest-paid user
*   top 3 salaries
*   count by city

Simple `find()` is not enough.

That’s where aggregation comes in.

---

# 2\. Aggregation Pipeline Concept

Aggregation works step-by-step.

```
db.collection.aggregate([
  { stage1 },
  { stage2 },
  { stage3 }
])
```

Each stage:

*   receives documents
*   modifies/filter/transforms them
*   passes output to next stage

---

# Visual Pipeline

```
Documents
   ↓
$match
   ↓
$group
   ↓
$sort
   ↓
$project
   ↓
Final Output
```

---

# 3\. Sample Dataset

We’ll use this throughout:

```
db.users.insertMany([
  {
    name: "Aman",
    age: 22,
    city: "Delhi",
    salary: 40000,
    skills: ["MongoDB", "Node.js"],
    active: true
  },
  {
    name: "Riya",
    age: 25,
    city: "Mumbai",
    salary: 60000,
    skills: ["React", "MongoDB"],
    active: true
  },
  {
    name: "Karan",
    age: 28,
    city: "Delhi",
    salary: 80000,
    skills: ["Python"],
    active: false
  }
])
```

---

# 4\. `$match` — Filtering Stage

Works like `find()`.

## Example

Find active users:

```
db.users.aggregate([
  {
    $match: {
      active: true
    }
  }
])
```

---

## Output

```
[
  {
    name: "Aman",
    active: true
  },
  {
    name: "Riya",
    active: true
  }
]
```

---

# Why `$match` Early Matters

Aggregation processes documents stage by stage.

Filtering early improves performance.

GOOD:

```
[
  { $match: { active: true } },
  { $group: ... }
]
```

BAD:

```
[
  { $group: ... },
  { $match: ... }
]
```

Because grouping huge data first is expensive.

---

# 5\. `$group` — Most Important Stage

Used for:

*   totals
*   averages
*   counting
*   analytics
*   reports

---

# Group Syntax

```
{
  $group: {
    _id: <grouping field>,
    fieldName: { operator }
  }
}
```

---

# Example — Count Users by City

```
db.users.aggregate([
  {
    $group: {
      _id: "$city",
      totalUsers: { $sum: 1 }
    }
  }
])
```

---

# How It Works

### Step 1

Input:

```
Delhi
Mumbai
Delhi
```

### Step 2

Grouped:

```
Delhi → 2
Mumbai → 1
```

---

# Output

```
[
  {
    _id: "Delhi",
    totalUsers: 2
  },
  {
    _id: "Mumbai",
    totalUsers: 1
  }
]
```

---

# Important Group Operators

| Operator | Meaning |
| --- | --- |
| `$sum` | total |
| `$avg` | average |
| `$max` | highest |
| `$min` | lowest |
| `$push` | collect into array |
| `$addToSet` | unique array |
| `$first` | first value |
| `$last` | last value |

---

# 6\. `$sum`

## Total Salary

```
db.users.aggregate([
  {
    $group: {
      _id: null,
      totalSalary: { $sum: "$salary" }
    }
  }
])
```

---

# Why `_id: null`?

Means:

> group everything together.

Equivalent to SQL:

```
SELECT SUM(salary) FROM users;
```

---

# Output

```
[
  {
    _id: null,
    totalSalary: 180000
  }
]
```

---

# 7\. `$avg`

## Average Salary

```
db.users.aggregate([
  {
    $group: {
      _id: null,
      averageSalary: { $avg: "$salary" }
    }
  }
])
```

---

# 8\. `$project` — Reshaping Documents

Very important stage.

Used for:

*   selecting fields
*   removing fields
*   renaming
*   computed values

---

# Example

```
db.users.aggregate([
  {
    $project: {
      name: 1,
      yearlySalary: {
        $multiply: ["$salary", 12]
      }
    }
  }
])
```

---

# Output

```
{
  name: "Aman",
  yearlySalary: 480000
}
```

---

# Why `1`?

```
name: 1
```

Means include field.

```
name: 0
```

Means exclude field.

---

# 9\. `$sort`

## Highest Salary First

```
db.users.aggregate([
  {
    $sort: {
      salary: -1
    }
  }
])
```

---

# Sort Values

| Value | Meaning |
| --- | --- |
| `1` | ascending |
| `-1` | descending |

---

# 10\. `$limit`

## Top 2 Users

```
db.users.aggregate([
  { $sort: { salary: -1 } },
  { $limit: 2 }
])
```

---

# 11\. `$skip`

Used for pagination.

## Skip First 5

```
db.users.aggregate([
  {
    $skip: 5
  }
])
```

---

# Pagination Example

Page 2 with 10 users:

```
[
  { $skip: 10 },
  { $limit: 10 }
]
```

---

# 12\. `$unwind` — Super Important

Used with arrays.

---

# Input

```
{
  name: "Aman",
  skills: ["MongoDB", "Node.js"]
}
```

---

# Query

```
db.users.aggregate([
  {
    $unwind: "$skills"
  }
])
```

---

# Output

```
{
  name: "Aman",
  skills: "MongoDB"
}

{
  name: "Aman",
  skills: "Node.js"
}
```

---

# Why Use `$unwind`?

Needed for:

*   counting array values
*   grouping array items
*   analytics on arrays

---

# Example — Skill Frequency

```
db.users.aggregate([
  { $unwind: "$skills" },
  {
    $group: {
      _id: "$skills",
      total: { $sum: 1 }
    }
  }
])
```

---

# Output

```
MongoDB → 2
Node.js → 1
Python → 1
```

---

# 13\. `$lookup` — MongoDB JOIN

Equivalent to SQL JOIN.

---

# users Collection

```
{
  _id: 1,
  name: "Aman"
}
```

---

# orders Collection

```
{
  userId: 1,
  product: "Laptop"
}
```

---

# Query

```
db.users.aggregate([
  {
    $lookup: {
      from: "orders",
      localField: "_id",
      foreignField: "userId",
      as: "orders"
    }
  }
])
```

---

# Output

```
{
  name: "Aman",
  orders: [
    { product: "Laptop" }
  ]
}
```

---

# Meaning of Fields

| Field | Meaning |
| --- | --- |
| `from` | other collection |
| `localField` | current collection field |
| `foreignField` | matching field |
| `as` | output array name |

---

# 14\. `$addFields`

Adds temporary/computed fields.

---

# Example

```
db.users.aggregate([
  {
    $addFields: {
      yearlySalary: {
        $multiply: ["$salary", 12]
      }
    }
  }
])
```

---

# Difference: `$project` vs `$addFields`

| `$project` | `$addFields` |
| --- | --- |
| reshapes document | adds fields |
| may remove fields | keeps original fields |

---

# 15\. Complex Real Pipeline

## Top Active Users

```
db.users.aggregate([
  {
    $match: {
      active: true
    }
  },
  {
    $sort: {
      salary: -1
    }
  },
  {
    $project: {
      name: 1,
      city: 1,
      salary: 1
    }
  },
  {
    $limit: 3
  }
])
```

---

# Pipeline Flow

```
All Users
   ↓
Only active users
   ↓
Sort by salary
   ↓
Select fields
   ↓
Take top 3
```

---

# 16\. Aggregation Expressions

Used inside:

*   `$project`
*   `$group`
*   `$addFields`

---

# Common Expressions

| Expression | Purpose |
| --- | --- |
| `$multiply` | multiplication |
| `$add` | addition |
| `$subtract` | subtraction |
| `$divide` | division |
| `$concat` | join strings |
| `$cond` | if-else |
| `$eq` | equals |
| `$gt` | greater than |

---

# Example — Bonus Calculation

```
db.users.aggregate([
  {
    $project: {
      name: 1,
      totalSalary: {
        $add: ["$salary", 5000]
      }
    }
  }
])
```

---

# 17\. `$cond` (IF ELSE)

## Example

```
db.users.aggregate([
  {
    $project: {
      name: 1,
      level: {
        $cond: {
          if: { $gte: ["$salary", 60000] },
          then: "Senior",
          else: "Junior"
        }
      }
    }
  }
])
```

---

# Output

```
Aman → Junior
Riya → Senior
```

---

# 18\. Aggregation Performance Tips

## Important Rules

### 1\. Use `$match` early

Reduces documents quickly.

---

### 2\. Use indexes

Especially on:

*   filter fields
*   sort fields

---

### 3\. Avoid unnecessary `$project`

Only select needed fields.

---

### 4\. Large `$lookup` can be expensive

Use carefully.

---

# 19\. Aggregation vs find()

| `find()` | Aggregation |
| --- | --- |
| simple queries | analytics |
| filtering | transformations |
| fast/simple | powerful |
| no grouping | grouping |

---

# 20\. SQL vs MongoDB Aggregation

## SQL

```
SELECT city, COUNT(*)
FROM users
GROUP BY city;
```

---

## MongoDB

```
db.users.aggregate([
  {
    $group: {
      _id: "$city",
      total: { $sum: 1 }
    }
  }
])
```

---

# 21\. Most Asked Interview Problems

---

## Find Duplicate Cities

```
db.users.aggregate([
  {
    $group: {
      _id: "$city",
      count: { $sum: 1 }
    }
  },
  {
    $match: {
      count: { $gt: 1 }
    }
  }
])
```

---

## Second Highest Salary

```
db.users.aggregate([
  { $sort: { salary: -1 } },
  { $skip: 1 },
  { $limit: 1 }
])
```

---

## City-wise Average Salary

```
db.users.aggregate([
  {
    $group: {
      _id: "$city",
      avgSalary: {
        $avg: "$salary"
      }
    }
  }
])
```

---

# 22\. Real-World Usage

Aggregation powers:

*   admin dashboards
*   analytics systems
*   ecommerce reports
*   charts
*   BI systems
*   recommendation engines
*   activity tracking
*   financial calculations
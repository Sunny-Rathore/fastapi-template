# Useful MongoDB Queries with Explanation

## 1. OR Query

Find documents where either `name` OR `email` matches the search value.

```js
const query = {
  $or: [
    { name: { $regex: search, $options: 'i' } },
    { email: { $regex: search, $options: 'i' } }
  ]
}
```

---

## 2. AND Query

Find documents where ALL conditions are true.

```js
const query = {
  $and: [
    { age: { $gte: 18 } },
    { status: 'active' }
  ]
}
```

---

## 3. Search Multiple Fields

Search across multiple fields using regex.

```js
const query = {
  $or: [
    { name: { $regex: search, $options: 'i' } },
    { email: { $regex: search, $options: 'i' } },
    { city: { $regex: search, $options: 'i' } }
  ]
}
```

---

## 4. Exact Match

Find documents with an exact value.

```js
const query = {
  email: 'test@gmail.com'
}
```

---

## 5. NOT Equal

Find documents where field value is NOT equal.

```js
const query = {
  status: { $ne: 'deleted' }
}
```

---

## 6. IN Operator

Find documents where value exists in an array.

```js
const query = {
  role: { $in: ['admin', 'manager'] }
}
```

---

## 7. NOT IN Operator

Exclude values from query results.

```js
const query = {
  role: { $nin: ['banned', 'blocked'] }
}
```

---

## 8. Greater Than / Less Than

Numeric comparisons.

```js
const query = {
  age: { $gt: 18 }
}
```

```js
const query = {
  age: { $lt: 60 }
}
```

```js
const query = {
  age: {
    $gte: 18,
    $lte: 60
  }
}
```

---

## 9. Field Exists

Find documents where field exists.

```js
const query = {
  phone: { $exists: true }
}
```

---

## 10. Field Does NOT Exist

Find documents without a field.

```js
const query = {
  phone: { $exists: false }
}
```

---

## 11. Null Check

Find documents where field is null.

```js
const query = {
  phone: null
}
```

---

## 12. Array Contains

Find array containing specific value.

```js
const query = {
  skills: 'Node.js'
}
```

---

## 13. Array Contains Multiple Values

Match all array values.

```js
const query = {
  skills: { $all: ['Node.js', 'MongoDB'] }
}
```

---

## 14. Array Size

Find arrays with specific length.

```js
const query = {
  skills: { $size: 3 }
}
```

---

## 15. Nested Object Query

Query nested fields using dot notation.

```js
const query = {
  'address.city': 'Delhi'
}
```

---

## 16. Regex Starts With

Find values starting with text.

```js
const query = {
  name: { $regex: '^john', $options: 'i' }
}
```

---

## 17. Regex Ends With

Find values ending with text.

```js
const query = {
  email: { $regex: 'gmail.com$', $options: 'i' }
}
```

---

## 18. Regex Contains

Find values containing text.

```js
const query = {
  name: { $regex: 'oh', $options: 'i' }
}
```

---

## 19. Date Range Query

Find documents within date range.

```js
const query = {
  createdAt: {
    $gte: new Date('2025-01-01'),
    $lte: new Date('2025-12-31')
  }
}
```

---

## 20. Sort Query

Sort documents ascending or descending.

```js
User.find(query).sort({ createdAt: -1 })
```

```js
.sort({ age: 1 })
```

---

## 21. Limit Query

Limit number of results.

```js
User.find().limit(10)
```

---

## 22. Pagination

Pagination using skip and limit.

```js
const page = 2
const limit = 10

User.find()
  .skip((page - 1) * limit)
  .limit(limit)
```

---

## 23. Select Specific Fields

Return selected fields only.

```js
User.find({}, 'name email')
```

Exclude fields:

```js
User.find({}, { password: 0 })
```

---

## 24. Count Documents

Count matching documents.

```js
User.countDocuments(query)
```

---

## 25. Distinct Values

Get unique field values.

```js
User.distinct('city')
```

---

## 26. Update One

Update single document.

```js
User.updateOne(
  { _id: id },
  { $set: { name: 'John' } }
)
```

---

## 27. Update Many

Update multiple documents.

```js
User.updateMany(
  { status: 'inactive' },
  { $set: { status: 'active' } }
)
```

---

## 28. Increment Value

Increase numeric value.

```js
User.updateOne(
  { _id: id },
  { $inc: { loginCount: 1 } }
)
```

---

## 29. Push Into Array

Add item to array.

```js
User.updateOne(
  { _id: id },
  { $push: { skills: 'React' } }
)
```

---

## 30. Pull From Array

Remove item from array.

```js
User.updateOne(
  { _id: id },
  { $pull: { skills: 'PHP' } }
)
```

---

## 31. Delete One

Delete single document.

```js
User.deleteOne({ _id: id })
```

---

## 32. Delete Many

Delete multiple documents.

```js
User.deleteMany({ status: 'deleted' })
```

---

## 33. Find One

Find first matching document.

```js
User.findOne({ email: 'test@gmail.com' })
```

---

## 34. Find By ID

Find document using ObjectId.

```js
User.findById(id)
```

---

## 35. Aggregate Match

Filter documents in aggregation.

```js
User.aggregate([
  {
    $match: {
      status: 'active'
    }
  }
])
```

---

## 36. Aggregate Group

Group documents and count.

```js
User.aggregate([
  {
    $group: {
      _id: '$city',
      total: { $sum: 1 }
    }
  }
])
```

---

## 37. Aggregate Project

Select fields in aggregation.

```js
User.aggregate([
  {
    $project: {
      name: 1,
      email: 1
    }
  }
])
```

---

## 38. Lookup (JOIN)

Join collections.

```js
Order.aggregate([
  {
    $lookup: {
      from: 'users',
      localField: 'userId',
      foreignField: '_id',
      as: 'user'
    }
  }
])
```

---

## 39. Unwind Array

Convert array items into documents.

```js
User.aggregate([
  {
    $unwind: '$skills'
  }
])
```

---

## 40. Text Search

Create text index:

```js
db.users.createIndex({
  name: 'text',
  email: 'text'
})
```

Search text:

```js
db.users.find({
  $text: {
    $search: 'john'
  }
})
```

---

## 41. Case-Insensitive Search

Case-insensitive exact search.

```js
const query = {
  username: {
    $regex: '^john$',
    $options: 'i'
  }
}
```

---

## 42. Dynamic Search Query

Build query dynamically.

```js
const query = {}

if (name) {
  query.name = { $regex: name, $options: 'i' }
}

if (email) {
  query.email = { $regex: email, $options: 'i' }
}

if (status) {
  query.status = status
}
```

---

## 43. Dynamic Filter + Pagination

Production-ready filtering.

```js
const query = {}

if (search) {
  query.$or = [
    { name: { $regex: search, $options: 'i' } },
    { email: { $regex: search, $options: 'i' } }
  ]
}

const users = await User.find(query)
  .sort({ createdAt: -1 })
  .skip((page - 1) * limit)
  .limit(limit)
```

---

## 44. Mongoose Populate

Populate referenced documents.

```js
Post.find()
  .populate('userId')
```

Specific fields:

```js
.populate('userId', 'name email')
```

---

## 45. Find Latest Record

Get newest document.

```js
User.findOne().sort({ createdAt: -1 })
```

---

## 46. Find Oldest Record

Get oldest document.

```js
User.findOne().sort({ createdAt: 1 })
```

---

## 47. Duplicate Detection

Find duplicate values.

```js
User.aggregate([
  {
    $group: {
      _id: '$email',
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

## 48. Conditional Query

Add conditions dynamically.

```js
const query = {
  isDeleted: false,
  ...(role && { role }),
  ...(status && { status })
}
```

---

## 49. ObjectId Query

Convert string to ObjectId.

```js
const mongoose = require('mongoose')

const query = {
  _id: new mongoose.Types.ObjectId(id)
}
```

---

## 50. Combine OR + AND

Use both AND and OR.

```js
const query = {
  $and: [
    { status: 'active' },
    {
      $or: [
        { name: { $regex: search, $options: 'i' } },
        { email: { $regex: search, $options: 'i' } }
      ]
    }
  ]
}
```

---

# Bonus: Production Query Example

Complete real-world query example.

```js
const query = {
  isDeleted: false
}

if (search) {
  query.$or = [
    { name: { $regex: search, $options: 'i' } },
    { email: { $regex: search, $options: 'i' } },
    { phone: { $regex: search, $options: 'i' } }
  ]
}

if (status) {
  query.status = status
}

const data = await User.find(query)
  .sort({ createdAt: -1 })
  .skip((page - 1) * limit)
  .limit(limit)
```

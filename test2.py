"""
jsonpath语法
$   根节点
@   表示当前节点
.   表示子节点
..  表示任意节点
[]  子节点选择
[,]
[start:end:step]
?()
"""
import jsonpath

dict1 = { "store": {
    "book": [
      { "category": "reference",
        "author": "Nigel Rees",
        "title": "Sayings of the Century",
        "price": 8.95
      },
      { "category": "fiction",
        "author": "Evelyn Waugh",
        "title": "Sword of Honour",
        "price": 12.99
      },
      { "category": "fiction",
        "author": "Herman Melville",
        "title": "Moby Dick",
        "isbn": "0-553-21311-3",
        "price": 8.99
      },
      { "category": "fiction",
        "author": "J. R. R. Tolkien",
        "title": "The Lord of the Rings",
        "isbn": "0-395-19395-8",
        "price": 22.99
      }
    ],
    "bicycle": {
      "color": "red",
      "price": 19.95
    }
  }
}

print(jsonpath.jsonpath(dict1, "$..author"))
print(jsonpath.jsonpath(dict1, "$..book[?(@.author=J. R. R. Tolkien)]"))

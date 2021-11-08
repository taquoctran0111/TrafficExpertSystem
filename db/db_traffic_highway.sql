/*
 Navicat Premium Data Transfer

 Source Server         : MongoDB
 Source Server Type    : MongoDB
 Source Server Version : 50003
 Source Host           : localhost:27017
 Source Schema         : db_traffic_highway

 Target Server Type    : MongoDB
 Target Server Version : 50003
 File Encoding         : 65001

 Date: 08/11/2021 14:30:36
*/


// ----------------------------
// Collection structure for cases
// ----------------------------
db.getCollection("cases").drop();
db.createCollection("cases");

// ----------------------------
// Documents of cases
// ----------------------------
db.getCollection("cases").insert([ {
    _id: ObjectId("6170e07d29e6433a0f981a8f"),
    Facts: [
        "Freeway"
    ],
    Conclusion: {
        Max: NumberInt("120"),
        Min: NumberInt("60")
    }
} ]);
db.getCollection("cases").insert([ {
    _id: ObjectId("6170e07d29e6433a0f981a90"),
    Facts: [
        "Freeway",
        "Two lanes",
        "Right lane"
    ],
    Conclusion: {
        Max: NumberInt("120"),
        Min: NumberInt("60")
    }
} ]);
db.getCollection("cases").insert([ {
    _id: ObjectId("6170e07d29e6433a0f981a91"),
    Facts: [
        "Freeway",
        "Two lanes",
        "Left lane"
    ],
    Conclusion: {
        Max: NumberInt("120"),
        Min: NumberInt("100")
    }
} ]);
db.getCollection("cases").insert([ {
    _id: ObjectId("6170e07d29e6433a0f981a92"),
    Facts: [
        "Freeway",
        "Three lanes",
        "Middle lane",
        "Safety distance 100 meters"
    ],
    Conclusion: {
        Max: NumberInt("100"),
        Min: NumberInt("90")
    }
} ]);
db.getCollection("cases").insert([ {
    _id: ObjectId("6170e07d29e6433a0f981a93"),
    Facts: [
        "Freeway",
        "Two lanes"
    ],
    Conclusion: {
        Max: NumberInt("120"),
        Min: NumberInt("60")
    }
} ]);
db.getCollection("cases").insert([ {
    _id: ObjectId("6170e07d29e6433a0f981a94"),
    Facts: [
        "Freeway",
        "100m"
    ],
    Conclusion: {
        Max: NumberInt("40")
    }
} ]);
db.getCollection("cases").insert([ {
    _id: ObjectId("6170e07d29e6433a0f981a95"),
    Facts: [
        "Freeway",
        "100m",
        "Three lanes",
        "Right lane"
    ],
    Conclusion: {
        Max: NumberInt("40")
    }
} ]);
db.getCollection("cases").insert([ {
    _id: ObjectId("6170e07d29e6433a0f981a96"),
    Facts: [
        "Freeway",
        "200m",
        "Two lanes",
        "Left lane"
    ],
    Conclusion: {
        Max: NumberInt("60")
    }
} ]);
db.getCollection("cases").insert([ {
    _id: ObjectId("6170e07d29e6433a0f981a97"),
    Facts: [
        "Freeway",
        "50m",
        "Three lanes",
        "Middle lane",
        "Safety distance 100 meters"
    ],
    Conclusion: {
        Max: NumberInt("20")
    }
} ]);
db.getCollection("cases").insert([ {
    _id: ObjectId("6170e07d29e6433a0f981a98"),
    Facts: [
        "Freeway",
        "100m",
        "Two lanes",
        "Right lane",
        "Safety distance 100 meters"
    ],
    Conclusion: {
        Max: NumberInt("40")
    }
} ]);
db.getCollection("cases").insert([ {
    _id: ObjectId("6170e07d29e6433a0f981a99"),
    Facts: [
        "Freeway",
        "Three lanes",
        "Right lane",
        "200m"
    ],
    Conclusion: {
        Max: NumberInt("60")
    }
} ]);

// ----------------------------
// Collection structure for rules
// ----------------------------
db.getCollection("rules").drop();
db.createCollection("rules");

// ----------------------------
// Documents of rules
// ----------------------------
db.getCollection("rules").insert([ {
    _id: ObjectId("6170e07d29e6433a0f981a83"),
    IF: [
        "Freeway"
    ],
    THEN: {
        Max: NumberInt("120"),
        Min: NumberInt("60")
    }
} ]);
db.getCollection("rules").insert([ {
    _id: ObjectId("6170e07d29e6433a0f981a84"),
    IF: [
        "Freeway",
        "Safety distance 100 meters"
    ],
    THEN: {
        Max: NumberInt("100")
    }
} ]);
db.getCollection("rules").insert([ {
    _id: ObjectId("6170e07d29e6433a0f981a85"),
    IF: [
        "Freeway",
        "Two lanes",
        "Left lane"
    ],
    THEN: {
        Min: NumberInt("100")
    }
} ]);
db.getCollection("rules").insert([ {
    _id: ObjectId("6170e07d29e6433a0f981a86"),
    IF: [
        "Freeway",
        "Three lanes",
        "Left lane"
    ],
    THEN: {
        Min: NumberInt("110")
    }
} ]);
db.getCollection("rules").insert([ {
    _id: ObjectId("6170e07d29e6433a0f981a87"),
    IF: [
        "Freeway",
        "Three lanes",
        "Middle lane"
    ],
    THEN: {
        Min: NumberInt("90")
    }
} ]);
db.getCollection("rules").insert([ {
    _id: ObjectId("6170e07d29e6433a0f981a88"),
    IF: [
        "Freeway",
        "Three lanes",
        "Right lane"
    ],
    THEN: {
        Max: NumberInt("60")
    }
} ]);
db.getCollection("rules").insert([ {
    _id: ObjectId("6170e07d29e6433a0f981a89"),
    IF: [
        "Freeway",
        "200m"
    ],
    THEN: {
        Max: NumberInt("60"),
        Advice: [
            "Open lights"
        ]
    }
} ]);
db.getCollection("rules").insert([ {
    _id: ObjectId("6170e07d29e6433a0f981a8a"),
    IF: [
        "Freeway",
        "100m"
    ],
    THEN: {
        Max: NumberInt("40"),
        Advice: [
            "Open lights"
        ]
    }
} ]);
db.getCollection("rules").insert([ {
    _id: ObjectId("6170e07d29e6433a0f981a8b"),
    IF: [
        "Freeway",
        "50m"
    ],
    THEN: {
        Max: NumberInt("20"),
        Advice: [
            "Open lights",
            "Leave ASAP"
        ]
    }
} ]);
db.getCollection("rules").insert([ {
    _id: ObjectId("6170e07d29e6433a0f981a8c"),
    IF: [
        "Freeway",
        "Slippery"
    ],
    THEN: {
        Max: NumberInt("40"),
        Advice: [
            "Slippery"
        ]
    }
} ]);
db.getCollection("rules").insert([ {
    _id: ObjectId("6170e07d29e6433a0f981a8d"),
    IF: [
        "Freeway",
        "High pass"
    ],
    THEN: {
        Max: NumberInt("40"),
        Advice: [
            "High pass"
        ]
    }
} ]);
db.getCollection("rules").insert([ {
    _id: ObjectId("6170e07d29e6433a0f981a8e"),
    IF: [
        "Freeway",
        "High pass",
        "Slippery"
    ],
    THEN: {
        Max: NumberInt("20"),
        Advice: [
            "High pass",
            "Slippery"
        ]
    }
} ]);
db.getCollection("rules").insert([ {
    _id: ObjectId("6188d19ad6c93bdf0ba2a1c6"),
    IF: "aaa",
    THEN: {
        Max: "121",
        Min: "1",
        Advice: "sds"
    }
} ]);

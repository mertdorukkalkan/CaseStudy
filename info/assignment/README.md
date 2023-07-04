### Assignment

A JSON representation of an SNMP MIB file is given. You are asked to restructure this JSON satisfying the requirements. You do not need to know about SNMP protocol or MIB files to complete this assignment, all the necessary information is given below. 

You may use the programming language of your choice to complete the assignment.


#### Before you begin
Given input file (`input.json`) is a JSON file generated from a MIB file, parsed and converted to JSON using pysmi library. MIB structure is hierarchical and an MIB objects' location in the hierarchy is defined by their OID number. If an object has an OID number `1.3.6`, that means this object is a child of the object with OID number `1.3`.

#### What we need?
Let's say we want to display the objects in the MIB in a tree form in the Web UI. And the UI tree component we use requires a specific data JSON schema in order to render properly. So, we need to restructure this JSON before serving it to the component. Check out the output JSON file (`output.json`).


#### Requirements
- `name` and `oid` should be present in the output JSON objects but attribute keys should be converted:
  - `name` -> `title`
  - `oid` -> `key`
- Do not include objects if:
  - they do not have an `oid` property.
  - their `class` is one of `notificationgroup`, `notificationtype`, `modulecompliance`, `objectgroup`.
  - their `status` is `deprecated`.
  
- Do not include parent objects if they are not defined in the file. For example, you do not need to create your tree starting from the object with OID `1`.
- `children` property should be an array containing the children objects of the object.
- If an object has no children, it should not have a `children` property.


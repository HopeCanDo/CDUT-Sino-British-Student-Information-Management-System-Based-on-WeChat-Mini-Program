'use strict';
const db = uniCloud.database();
exports.main = async (event, context) => {
	const collection = db.collection("users");//Table users with corresponding names for operations
	const res = await collection.where({
		user_name:event.user_name
	}).get();//Similar to SQL, query statements are followed by conditions. Assign the query results to res
	let status=0;//Used to mark status
	console.log('res:',res)//Print res to view received styles
	let user = res.data; 
	if (user.length != 0) {//If the length in the user array found based on the username is not 0, it indicates that the username already exists.
		status = 1;
	} else{//If the username is not duplicated, add user information to the database
		let res =await collection.add({"user_name":event.user_name,"password":event.password});
	}
	return {"status":status}//0- The username does not have 'registration successful'; 1- The username already exists;
};
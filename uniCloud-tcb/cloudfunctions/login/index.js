'use strict';
const db = uniCloud.database();

exports.main = async (event, context) => { //event is the parameter uploaded by the client
	const collection = db.collection("users"); //Table users with corresponding names for operations
	const res = await collection.where({
		user_name: event.user_name
	}).get();//Similar to SQL, query statements are followed by conditions. Assign the query results to res
	let status = 0; //Used to mark status
	let user = res.data;
	if (user.length == 0) {
		status = 1;
	}//Unable to find, username does not exist.
	if (user.length != 0 && user[0].password != event.password) {
		status = 2;
	} //Found, but the password does not match the password in the table memory.
	return {//0- Login successful; 1- The username does not exist; 2- Password error;
		"status": status,
		"user_name":event.user_name
	}
};
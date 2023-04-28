'use strict';
exports.main = async (event, context) => {
	//event is the parameter uploaded by the client
	console.log('event : ', event)
	let callback =[];
	const db = uniCloud.database();
	const collection = db.collection("note"); 
	await collection.add({
		content:event.content,
		user_name:event.user_name,
		createdtime:event.createdtime
	})
	callback={
		code:1,
		msg:"success"
	}
	//return data to the client
	return callback
	
};

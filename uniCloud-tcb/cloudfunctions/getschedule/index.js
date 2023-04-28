'use strict';
exports.main = async (event, context) => {
	//event is the parameter uploaded by the client
	console.log('event : ', event)
	const db = uniCloud.database();
	const collection = db.collection("schedule"); 
	let rs = await collection.where({user_name:event.user_name}).get();
	//return data to the client
	return rs
};

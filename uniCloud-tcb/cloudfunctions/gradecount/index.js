'use strict';
exports.main = async (event, context) => {
	//event is the parameter uploaded by the client
	console.log('event : ', event)
	const db = uniCloud.database();
	const collection =await db.collection("grade"); 
	let res = await collection.where({user_name:event.user_name}).count();
	//return data to the client
	return res
};

'use strict';
exports.main = async (event, context) => {
	//event is the parameter uploaded by the client
	console.log('event : ', event)
	const db = uniCloud.database();
	const collection = await db.collection("userinfo");

	let res = await collection.where({
		user_name:event.user_name
	}).update({
		gender: event.gender
	})
	//return data to the client
	return res
};
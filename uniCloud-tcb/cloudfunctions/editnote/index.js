'use strict';
exports.main = async (event, context) => {
	//event is the parameter uploaded by the client
	console.log('event : ', event)
	const db = uniCloud.database();
	const collection =await db.collection("note"); 
	
	let res = await collection.where({_id:event.note_id}).update({content:event.note_content})
	//return data to the client
	return res
};

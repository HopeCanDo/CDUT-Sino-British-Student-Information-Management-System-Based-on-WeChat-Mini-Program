'use strict';
exports.main = async (event, context) => {
	//event is the parameter uploaded by the client
	console.log('event : ', event)
	var filter={user_name:event.user_name};
	const db = uniCloud.database();
	const collection = db.collection("grade"); 
	var arr =Object.keys(event.keyword);
	if(arr.length>0){
		filter={content:new RegExp(event.keyword)}
	}
	let rs = await collection.where(filter).orderBy('createdtime','desc').get();
	//return data to the client
	return rs
};

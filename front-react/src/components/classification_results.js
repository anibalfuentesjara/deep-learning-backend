import React, {useState} from 'react';
import ReactDOM from 'react-dom';

const ClassificationResult = ({result}) => {
	return (
		<div>
			<p> Name: {result.class_name} </p>
			<p> Probability: {result.class_probability} </p>
		</div>
	);
}

const displayClassificationResults = ({results}) => {
	if (results && results.classification_results)
		return results.classification_results.map(result => {return <ClassificationResult result={result} />});
	else
		return <div />
}

const ClassificationResults = ({results}) => {
	return displayClassificationResults({results});
}

export default ClassificationResults;
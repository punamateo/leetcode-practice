// https://leetcode.com/problems/flood-fill/description/

/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} color
 * @return {number[][]}
 */

var getMapKey = function(sr, sc) {
    return sr.toString() + sc.toString();
}

var getAdjacentIndexes = function(image, sr, sc){
    const adjacentIndexes = [];

    const prevRow = sr - 1;
    const nextRow = sr + 1;
    const prevCol = sc - 1;
    const nextCol = sc + 1;

    if (prevRow >= 0) {
        adjacentIndexes.push([prevRow, sc]);
    } 

    if (prevCol >= 0) {
        adjacentIndexes.push([sr, prevCol]);
    }

    if (nextRow < image.length) {
        adjacentIndexes.push([nextRow, sc]);
    }

    if (nextCol < image[0].length) {
        adjacentIndexes.push([sr, nextCol]);
    }

    return adjacentIndexes;
}

var getAdjacentNotPaintedPixels = function(image, sr, sc, color, startPixelColor){

    const adjacentIndexes = getAdjacentIndexes(image,sr, sc);

    return adjacentIndexes.filter(index => {
        const row = index[0];
        const col = index[1];
        return image[row][col] == startPixelColor; 
    });
}

var floodFill = function(image, sr, sc, color) {

// start process to flood
const startPixelColor = image[sr][sc];

if (color != startPixelColor) {
    image[sr][sc] = color;
    // pixelsMap.set(getMapKey(sr,sc), color);
}

recursiveFloodFill(image, sr, sc, color, startPixelColor)

return image

};


var recursiveFloodFill = function(image, sr, sc, color, startPixelColor) {
    const adjacentNotPaintedPixels = getAdjacentNotPaintedPixels(image, sr, sc, color, startPixelColor);
    if (adjacentNotPaintedPixels.length <= 0) {
        return;
    }

    for (var i = 0; i < adjacentNotPaintedPixels.length; i++) {
        pixelRow = adjacentNotPaintedPixels[i][0];
        pixelCol = adjacentNotPaintedPixels[i][1];
        // const pixelMapKey = getMapKey(pixelRow, pixelCol);

        if (color != startPixelColor) {
            image[pixelRow][pixelCol] = color;
            recursiveFloodFill(image,pixelRow,pixelCol,color,startPixelColor);
            // pixelsMap.set(pixelMapKey, color);

        }
    }
};

const m1 = [[1,1,1],[1,1,0],[1,0,1]];
const m2 = [[0,0,0],[0,0,0]];


const coloredM1 = floodFill(m1,1,1,2);
const coloredM2 = floodFill(m2,0,0,0);

console.log(coloredM1);
console.log(coloredM2);


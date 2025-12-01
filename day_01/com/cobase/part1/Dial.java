package com.cobase.part1;

public class Dial {
    private static final int MAX_DIAL_VALUE = 100;

    private int currentPointer;

    public Dial(int currentPointer) {
        this.currentPointer = currentPointer;
    }
    
    public void turnLeft(int distance) {
        this.currentPointer = Math.abs(currentPointer - (distance % MAX_DIAL_VALUE) + MAX_DIAL_VALUE) % MAX_DIAL_VALUE;
    }

    public void turnRight(int distance) {
        this.currentPointer = (this.currentPointer + (distance % MAX_DIAL_VALUE)) % MAX_DIAL_VALUE;
    }

    public boolean isAtPosZero() {
        return this.currentPointer == 0;
    }

    public int getCurrentPointer() {
        return currentPointer;
    }
}
